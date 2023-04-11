from sortedcontainers import SortedList
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        res = 0
        # do dec instead of inc
        mn = min(nums)
        for i in nums:
            res+=abs(i-mn)
        return res