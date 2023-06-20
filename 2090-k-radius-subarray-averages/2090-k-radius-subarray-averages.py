class Solution:
    def getAverages(self, nums: List[int], k: int) -> List[int]:
        p = 0
        res = []
        for i in range(len(nums)):
            p+=nums[i]
            nums[i] = p
        size = 2*k + 1
        def computeSum(a,b):
            if a==0:
                return nums[b]
            return nums[b] - nums[a-1]
            
        for i in range(len(nums)):
            if i-k>=0 and i+k<len(nums):
                res.append(computeSum(i-k,i+k)//size)
            else:
                res.append(-1)
        return res