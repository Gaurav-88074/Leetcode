class Solution {
    private boolean[] visited;
    public void DFS(int start,int[][] graph){
        visited[start] = true;
        for(int i = 0 ; i<graph.length ; i++){
            if(graph[start][i]==1 && visited[i]==false){
                DFS(i,graph);
            }
        }
    }
    public int findCircleNum(int[][] isConnected) {
        int res = 0;
        visited = new boolean[isConnected.length];
        for(int i =0 ; i<visited.length ; i++){
            if(visited[i]==false){
                DFS(i,isConnected);
                res+=1;
            }
            
        }
        return res;
    }
}