class Solution:
    def minimumDeleteSum(self, s1: str, s2: str) -> int:
        @lru_cache(None)
        def computeLCS(i,j):
            if i==-1 or j==-1 :
                return 0
            if s1[i]==s2[j]:
                return ord(s1[i]) + computeLCS(i-1,j-1)
            else:
                left = computeLCS(i-1,j)
                right= computeLCS(i,j-1)
                return max(left,right)
        lcs = computeLCS(len(s1)-1,len(s2)-1)
        
        totalSum =0
        for i in s1:
            totalSum+=ord(i)
        for i in s2:
            totalSum+=ord(i)
        return totalSum- 2*lcs