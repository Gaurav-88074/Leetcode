class Solution:
    def unequalTriplets(self, nums: List[int]) -> int:
        res= 0
        g = set()
        n = len(nums)
        for i in range(n):
            for j in range(i+1,n):
                for k in range(j+1,n):
                    s = set()
                    s.add(nums[i])
                    s.add(nums[j])
                    s.add(nums[k])
                    # if nums[i]>nums[j]>nums[k]:
                    v = (nums[i],nums[j],nums[k])
                    if len(s)==3  :
                        res+=1
                        g.add(v)
        return res
                        