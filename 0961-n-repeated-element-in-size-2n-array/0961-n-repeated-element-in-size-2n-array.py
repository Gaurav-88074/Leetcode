class Solution:
    def repeatedNTimes(self, nums: List[int]) -> int:
        res = []
        c=Counter(nums)
        n = len(nums)//2
        for i in c:
            if c[i]==n:
                return i
        return -1