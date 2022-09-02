class Solution:
    def findLonely(self, nums: List[int]) -> List[int]:
        c = Counter(nums)
        s =set(nums)
        res = []
        for i in nums:
            if not i+1 in s and not i-1 in s and c[i]==1:
                res.append(i)
                
        return res