class Solution:
    def maxValueOfCoins(self, piles: List[List[int]], k: int) -> int:
        @lru_cache(None)
        def compute(index,k):
            if k<0:
                return -1
            if k==0 or index==len(piles):
                return 0
            
            skip = compute(index + 1,k)
            take = 0
            val = 0
            for i in range(len(piles[index])):
                val+=piles[index][i]
                takeTemp = compute(index+1,k-i-1)
                if takeTemp!=-1:
                    takeTemp+=val
                    take = max(take,takeTemp)
            return max(take,skip)
        return compute(0,k)
            