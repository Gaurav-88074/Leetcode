
class Solution:
    def maxScore(self, nums: List[int], x: int) -> int:
        # 1->odd
        # 0->even
        @lru_cache(None)
        def compute(i,parity):
            if i==len(nums):
                return 0
            take1 = 0
            take2 = 0
            if nums[i]%2==parity:
                take1 =      nums[i]+compute(i+1,nums[i]%2)
            if nums[i]%2!=parity:
                take2 = -x + nums[i]+compute(i+1,nums[i]%2)
            skip = compute(i+1,parity)
            return max(take1,take2,skip)
        res = nums[0]+compute(1,nums[0]%2)
        return res