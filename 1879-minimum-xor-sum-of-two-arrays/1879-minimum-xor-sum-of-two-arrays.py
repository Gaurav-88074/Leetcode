class Solution(object):
    def minimumXORSum(self, nums1, nums2):
        n = len(nums1)
        def isUsed(mask,i):
            return (mask & (1<<i))>0
        dp ={}
        def compute(i,mask_a,mask_b):
            if mask_a== (1<<n)-1:
                return 0
            key = (i,mask_a,mask_b)
            if key in dp : return dp[key]
            res = float('inf')
            v = nums1[i]
            for j,w in enumerate(nums2):
                if not isUsed(mask_a,i) and not isUsed(mask_b,j):
                    temp = (v^w) + compute(i+1,mask_a|(1<<i) , mask_b|(1<<j))
                    res =min(temp,res)
            dp[key] = res
            return res
        res = compute(0,0,0)
        return res
        