class Ocean{
    public boolean pacificOcean;
    public boolean atlanticOcean;
    public Ocean(){
        this.pacificOcean  = false;
        this.atlanticOcean = false;
    }
    public Ocean(boolean a,boolean b){
        this.pacificOcean  = a;
        this.atlanticOcean = b;
    }
    public void OR(Ocean obj){
        this.pacificOcean  = this.pacificOcean  || obj.pacificOcean;
        this.atlanticOcean = this.atlanticOcean || obj.atlanticOcean;
    }
    public boolean check(){
        return (this.pacificOcean==true && this.atlanticOcean==true);
    }
    public String toString(){
        return String.valueOf(pacificOcean)+" : "+String.valueOf(atlanticOcean==true);
    }
}
class Solution {
    private List<List<Integer>> res = new LinkedList<>();
    private Ocean[][] dp; 
    
    private int[][] visited;
    public Ocean compute(int[][] matrix,int x,int y,int that){
        if(x==-1 || y==-1){
            return new Ocean(true,false); 
        }
        if(x==matrix.length || y==matrix[0].length){
            return new Ocean(false,true); 
        }
        
        if(visited[x][y]==1) return new Ocean(false,false);
        
    
        if(matrix[x][y]>that){
            return new Ocean(false,false);
        }
         //-------------------------------
        Ocean obj = new Ocean();
        //-------------------------------
        //------------------------
        
        if(dp[x][y]!=null){
            obj.OR(dp[x][y]);
            if(obj.check()){
                return obj;
            }
        }
            
            
        //------------------------
        
       
        visited[x][y] = 1;
        //-------------------------------
        int org = matrix[x][y];
        
        if(!obj.check()){
            Ocean left  = compute(matrix,x,y-1,org);
            obj.OR(left);
        }
        
        
        if(!obj.check()){
            Ocean right = compute(matrix,x,y+1,org);
            obj.OR(right);
        }
        
        
        if(!obj.check()){
            Ocean top   = compute(matrix,x-1,y,org);
            obj.OR(top);
        }
        
        
        if(!obj.check()){
            Ocean down  = compute(matrix,x+1,y,org);
            obj.OR(down);
        }
        
        
        //---------------
        visited[x][y] = 0;
        //---------------
        
        dp[x][y] = obj;
        
        
        
        return obj;
    }
    public List<List<Integer>> pacificAtlantic(int[][] matrix) {
        dp = new Ocean[matrix.length][matrix[0].length];
        visited = new int[matrix.length][matrix[0].length];
        for(int i = 0 ; i<matrix.length ; i++){
            for(int j = 0 ; j<matrix[0].length ; j++){
                // dp[i][j]=null;
                Ocean check = compute(matrix,i,j,matrix[i][j]);
                // dp[i][j]=null;
                // dpState(dp);
                if(check.check()){
                    // dp[i][j]=null;
                    Integer a[] = new Integer[] {i,j};
                    res.add(Arrays.asList(a));
                    // System.out.println(i+" - "+j);
                }
            }
        }
        return res;
    }
    public void dpState(Ocean[][] dp){
        System.out.println("----------------------");
        for(int i = 0 ; i<dp.length ; i++){
            for(int j = 0 ; j<dp[0].length ; j++){
               System.out.print(dp[i][j]+"  ");
            }
            System.out.println();
        }
        System.out.println("----------------------");
    }
}