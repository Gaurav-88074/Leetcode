class Solution:
    def minimumDeletions(self, nums: List[int]) -> int:
        mn = min(nums)
        mx = max(nums)
        
        a = nums.index(mn)
        b = nums.index(mx)
        if a>b:
            a,b=b,a
        r1 = a+1
        r2 = len(nums)-b
        
        r3 = b+1
        r4 = len(nums)-a
        
        return min(r1+r2,r3,r4)
        