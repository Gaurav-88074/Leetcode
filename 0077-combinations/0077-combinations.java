class Solution {
    private List<Integer> array = new ArrayList<>();
    private List<List<Integer>> res  =  new ArrayList<>(); 
    public void combinationOfSizeK(int index,int k,int n){
        if (k==0) {
            res.add(new ArrayList(array));
            // System.out.println(array);
            return;
        }
        for (int i = index; i <=n; i++) {
            array.add(i);
            combinationOfSizeK(i+1, k-1, n);
            array.remove(array.size()-1);
        }
    }
    public List<List<Integer>> combine(int n, int k) {
        combinationOfSizeK(1,k,n);
        return this.res;
    }
}