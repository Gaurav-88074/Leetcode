class Solution:
    def findSubarrays(self, nums: List[int]) -> bool:
        res = []
        for i in range(len(nums)-1):
            res.append(nums[i] + nums[i+1])
        c = Counter(res)
        for i in c:
            if c[i]>=2:
                return True
        return False