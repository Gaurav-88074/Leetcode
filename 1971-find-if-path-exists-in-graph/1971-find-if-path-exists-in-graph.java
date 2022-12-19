class Solution {
    public  void BFS(List<List<Integer>> graph,int[] visited,int start,int d) {
        // int[] visited = new int[graph.size()];
        visited[start] = 1;
        Queue<Integer> queue = new LinkedList<>();
        queue.add(start);
        // System.out.print(start+"->");
        while (!queue.isEmpty()) {
            int node = queue.poll();
            for (int j : graph.get(node)){
                if (visited[j]==0) {
                    visited[j]=1;
                    if(visited[d]==1){
                        return;
                    }
                    queue.add(j);
                }
            }
        }
        // System.out.println();
    }
    public boolean validPath(int n, int[][] edges, int source, int destination) {
        List<List<Integer>> graph = new ArrayList<>();
        for(int i =  0; i<n; i++){
            graph.add(new LinkedList<>());
        }
        // System.out.println(graph);
        for(int i =  0; i<edges.length; i++){
            // System.out.println(graph);
            graph.get(edges[i][0]).add(edges[i][1]);
            graph.get(edges[i][1]).add(edges[i][0]);
        }
        // System.out.println(graph);
        // System.out.println(source+"-"+destination);
        int[] visited = new int[n];
        BFS(graph,visited,source,destination);
        return visited[destination]==1;
        
    }
}