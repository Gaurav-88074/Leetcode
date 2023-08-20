class Solution:
    def minimumXORSum(self, nums1: List[int], nums2: List[int]) -> int:
        n = len(nums1)
        def isUsed(mask,i):
            return (mask & (1<<i))>0
        @lru_cache(None)
        def compute(i,mask_a,mask_b):
            if mask_a== (1<<n)-1:
                return 0
            res = float('inf')
            v = nums1[i]
            for j,w in enumerate(nums2):
                if not isUsed(mask_a,i) and not isUsed(mask_b,j):
                    temp = (v^w) + compute(i+1,mask_a|(1<<i) , mask_b|(1<<j))
                    res =min(temp,res)
            return res
        res = compute(0,0,0)
        compute.cache_clear()
        return res
        #-----------------------------------
        #This will also work
        #-----------------------------------
        # @lru_cache(None)
        # def compute(mask_a,mask_b):
        #     if mask_a== (1<<n)-1:
        #         return 0
        #     i = bin(mask_a)[2:].count('1')
        #     res = float('inf')
        #     v = nums1[i]
        #     for j,w in enumerate(nums2):
        #         if not isUsed(mask_a,i) and not isUsed(mask_b,j):
        #             temp = (v^w) + compute(mask_a|(1<<i) , mask_b|(1<<j))
        #             res =min(temp,res)
        #     return res
        # res = compute(0,0)
        # compute.cache_clear()
        # return res