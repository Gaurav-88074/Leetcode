class Solution {
    public int xorAllNums(int[] nums1, int[] nums2) {
        int v = 0;
        //top part
        int i;
        if(nums2.length%2!=0){
            i = 0;
            while(i<nums1.length){
                v=v^nums1[i++];
            }
        }
        //bottom part
        // int i;
        if(nums1.length%2!=0){
            i = 0;
            while(i<nums2.length){
                v=v^nums2[i++];
            }
        }
        //ans part
        return v;
    }
}