class Solution {
    
    public int getPeakIndex(int[] col) {
        int maxIndex = -1, maxElement = Integer.MIN_VALUE;
        
        for(int i =0; i < col.length; i++) {
            if(maxElement < col[i]) {
                maxIndex = i;
                maxElement = col[i];
            }
        }
        
        return maxIndex;
    }
    
    public int[] findPeakGrid(int[][] mat) {
        int r = mat.length, c = mat[0].length;
        int low = 0, high = r-1;
        
        if(low == high) {
            return new int[]{low, getPeakIndex(mat[0])};
        }
        
        while(low <= high) {
            int mid = (low+high)/2;
            
            int peakIndex = getPeakIndex(mat[mid]);
            
            if(mid < r-1 && mat[mid][peakIndex] < mat[mid+1][peakIndex]) {
                low = mid +1;
            } else if(mid > 0 && mat[mid][peakIndex] < mat[mid-1][peakIndex]) {
                high = mid -1;
            } else{
                return new int[]{mid, peakIndex};
            }
        }
        
        return new int[]{-1,-1};
    }
}