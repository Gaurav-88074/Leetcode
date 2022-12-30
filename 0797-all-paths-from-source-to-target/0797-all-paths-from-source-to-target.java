class Solution {
    // private boolean[] visited;
    private int dest;
    private List<Integer> l = new ArrayList<>();
    private List<List<Integer>> res = new ArrayList<>();
    
    public void go(int[][] graph,int source){
        l.add(source);
        if(source==dest){
            // System.out.println(l);
            res.add(new ArrayList<>(l) );
            l.remove(l.size()-1);
            return;
        }
        
        for(int node : graph[source]){
            // if(visited[node]==false){
            //     visited[node] = true;
                
                go(graph,node);
                
            //     visited[node] = false;
            // }
        }
        l.remove(l.size()-1);
    }
    public List<List<Integer>> allPathsSourceTarget(int[][] graph) {
        // visited = new boolean[graph.length];
        dest = graph.length-1;
        
        go(graph,0);
        
        return res;
        
    }
}