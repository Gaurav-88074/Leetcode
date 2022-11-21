class Solution:
    def findDisappearedNumbers(self, nums: List[int]) -> List[int]:
        res = set([i for i in range(1,len(nums)+1)])
        for i in nums:
            res.discard(i)
        return res