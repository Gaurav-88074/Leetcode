class Solution {
    public long coloredCells(int n) {
        if(n==1)return n;
        return 4*(n-1) + coloredCells(n-1);
    }
}