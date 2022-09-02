class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        s = Counter(nums)
        res = []
        for i in nums:
            if not i+1 in s and not i-1 in s and s[i]==1:
                res.append(i)
                
        return res