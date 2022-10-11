class Solution:
    def increasingTriplet(self, nums: List[int]) -> bool:
        l = [ float('inf'),float('inf') ]
        for i in nums:
            if i<l[0]:
                l[0] = i
            if i<l[1] and i>l[0]:
                l[1] = i
            if i>l[1]:
                return True
        return False