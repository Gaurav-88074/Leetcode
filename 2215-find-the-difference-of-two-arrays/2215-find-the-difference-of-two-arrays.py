class Solution:
    def findDifference(self, nums1: List[int], nums2: List[int]) -> List[List[int]]:
        a=set(nums1)
        b=set(nums2)
        e= a.intersection(b)
        c=set()
        d=set()
        for i in nums1:
            if i not in e:
                c.add(i)
        for i in nums2:
            if i not in e:
                d.add(i)
        return [list(c),list(d)]