class Solution(object):
    def findNonMinOrMax(self, nums):
        minimum = maximum = nums[0]

        for num in nums[1:]:
            minimum = min(minimum, num)
            maximum = max(maximum, num)

        for num in nums:
            if num != minimum and num != maximum:
                return num

        return -1
        