class Solution {
    public List<Integer> goodIndices(int[] num, int k) {
        int[] left=new int[num.length];
        int[] right=new int[num.length];
        left[num.length-1]=1;
        for(int i=num.length-2;i>=0;i--){
            if(num[i]<=num[i+1]){
                left[i]=left[i+1]+1;
            }else{
                left[i]=1;
            }
        }

        right[0]=1;
        for(int i=1;i<num.length;i++){
            if(num[i]<=num[i-1]){
                right[i]=right[i-1]+1;
            }else{
                right[i]=1;
            }
        }
        List<Integer> res=new ArrayList<>();
        for(int i=1;i<num.length-1;i++){
            if(left[i+1]>=k && right[i-1]>=k){
                res.add(i);
            }
        }
        return res;
    }
}