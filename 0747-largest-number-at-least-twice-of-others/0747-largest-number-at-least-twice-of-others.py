class Solution:
    def dominantIndex(self, nums: List[int]) -> int:
        m = max(nums)
        v = float('-inf')
        for i in nums:
            if i!=m:
                v=max(v,i)
        return nums.index(m)  if m>=(2*v)  else -1