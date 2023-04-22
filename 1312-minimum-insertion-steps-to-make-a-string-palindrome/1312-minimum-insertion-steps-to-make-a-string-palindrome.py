class Solution:
    def minInsertions(self, s: str) -> int:
        a=s
        b=s[::-1]
        n=len(s)
        @lru_cache(None)
        def compute(i,j):
            if i==n or j==n:
                return 0
            if a[i]==b[j]:
                v=1+compute(i+1,j+1)
                return v
            else:
                left=compute(i+1,j)
                righ=compute(i,j+1)
                return max(left,righ)
        val =compute(0,0)
        #print(val)
        return n-val