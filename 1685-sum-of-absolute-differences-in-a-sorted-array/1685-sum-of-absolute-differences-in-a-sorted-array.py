class Solution:
    def getSumAbsoluteDifferences(self, nums: List[int]) -> List[int]:
        s = sum(nums)
        prefix=[]
        v =0
        for i in nums:
            v+=i
            prefix.append(v)
        
        res = []
        for i in range(len(nums)):
            value = nums[i]
            
            leftSum  = prefix[i]
            rightSum = s-prefix[i]
            
            ans = abs(leftSum - (value*(i+1)))
            ans += abs(rightSum - (value*(len(nums) - i-1)))
            
            res.append(ans)
        return res