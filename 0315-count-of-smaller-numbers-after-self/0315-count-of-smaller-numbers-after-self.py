from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        l = SortedList()
        res = [0]*len(nums)
        for i in range(len(nums)-1,-1,-1):
            value = nums[i]
            bi = l.bisect_left(value)
            res[i] = bi
            l.add(value)
        return res