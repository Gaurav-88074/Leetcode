class Solution {
    public int findRadius(int[] houses, int[] heaters) {
        TreeSet<Integer> set = new TreeSet<>();
        for(int i : heaters){
            set.add(i);
        }
        int res = 0;
        Integer left;
        Integer right;
        for(int v : houses){
            left = set.floor(v);
            right= set.ceiling(v);
            if(left==null){
                res = Math.max( res, right-v);
            }
            else if(right==null){
                res = Math.max( res, v-left);
            }
            else{
                res = Math.max( res, Math.min(v-left,right-v));
            }
        }
        return res;
    }
}