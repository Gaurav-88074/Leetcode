class Solution:
    def findNonMinOrMax(self, nums: List[int]) -> int:
        if len(nums)<=2:
            return -1
        # nums.sort()
        # return nums[1]
        mn = min(nums)
        mx = max(nums)
        nums.remove(mn)
        nums.remove(mx)
        return random.choice(nums)
        