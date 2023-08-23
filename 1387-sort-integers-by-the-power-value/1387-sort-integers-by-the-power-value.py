class Solution:
    def getKth(self, lo: int, hi: int, k: int) -> int:
        
        @lru_cache(None)
        def compute(n):
            if n==1:
                return 0
            if (n&1)==1:
                return 1 + compute(3*n+1)
            else:
                return 1 + compute(n//2)
        nums = []
        for i in range(lo,hi+1):
            nums.append(i)
        nums.sort(key = lambda x : compute(x))#use brain
        # print(nums)
        return nums[k-1]