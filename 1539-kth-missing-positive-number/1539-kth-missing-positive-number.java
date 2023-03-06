class Solution {
    public int findKthPositive(int[] arr, int k) {
        int[] array = new int[1001];
        for(int i : arr){
            array[i]=1;
        }
        for(int i=1 ; i<1001;i++){
            if(array[i]==0){
                k--;
            }
            if(k==0){
                return i;
            }
        }
        return k+1000;
    }
}