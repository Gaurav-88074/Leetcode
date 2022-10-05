class Solution {
    public int hIndex(int[] array) {
        // Arrays.sort(array);
        // System.out.println(Arrays.toString(array));
        
        int res = 0;
        
        int ii=0;
        int n = array.length;
        for(int value : array){
            if(n-ii <= value){
                res+=1;
            }
            ii+=1;

        }
        return res;
    }
}