class Solution {
    public int trap(int[] height) {
        if(height.length==0){
            return 0;
        }
        int[] leftToRight = new int[height.length];
        int[] rightToLeft = new int[height.length];
        int temp1 = height[0]; 
        int temp2 = height[height.length-1];
        for(int i = 0 ; i<height.length ; i++){
            if(height[i]>temp1){
                temp1=height[i];
            }
            leftToRight[i]=temp1;
        }
        for(int i = height.length-1 ; i>=0 ; i--){
            if(height[i]>temp2){
                temp2=height[i];
            }
            rightToLeft[i]=temp2;
        }
        int res=0;
        for(int i = 0 ; i<height.length ; i++){
            res+= Math.abs(Math.min(leftToRight[i],rightToLeft[i])-height[i]);
        }
        return res;
    }
}