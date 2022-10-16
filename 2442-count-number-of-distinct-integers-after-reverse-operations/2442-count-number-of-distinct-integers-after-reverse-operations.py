class Solution:
    def countDistinctIntegers(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            v = str(nums[i])
            v = v[::-1]
            nums.append(int(v))
        # print(nums)
        return len(set(nums))