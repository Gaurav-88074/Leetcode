class Solution:
    def coloredCells(self, n: int) -> int:
        
        def compute(n):
            if n==1:
                return n
            return 4*(n-1) + compute(n-1)
        return compute(n)