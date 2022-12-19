class Solution:
    def numSubarraysWithSum(self, nums: List[int], goal: int) -> int:
        res = 0
        psum = 0
        d =defaultdict(int)
        for i,v in enumerate(nums):
            d[psum]+=1
            psum+=v
            res+=d[psum-goal]
        return res