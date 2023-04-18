class Solution:
    def sumOfUnique(self, nums: List[int]) -> int:
        return sum([i for i,v in Counter(nums).items() if v==1])