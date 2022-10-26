class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        d = defaultdict(int)
        pre = 0
        for i in range(len(nums)):
            pre+=nums[i]
            
            mod = pre%k
            
            if i>=1 and mod==0 :
                return True
            if mod in d and i-d[mod]>=2:
                return True
            if mod not in d :
                d[mod] = i
        return False