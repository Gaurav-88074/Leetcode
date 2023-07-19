class Solution {
    public int eraseOverlapIntervals(int[][] intervals) {
        Arrays.sort(intervals,(a,b)->(a[1] - b[1]));
        
        int res = 0;
        int pre  =-100000;
        for(int[] i : intervals){
            if(i[0] < pre){
                // System.out.println(Arrays.toString(i));
                // System.out.println(i[0]+" < "+pre);
                res+=1;
                continue;
            }
            pre = i[1];
        }
        return res;
    }
}