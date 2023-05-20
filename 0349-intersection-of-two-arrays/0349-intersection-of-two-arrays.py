class Solution:
    def intersection(self, nums1: List[int], nums2: List[int]) -> List[int]:
        # a = set(nums1)
        # b = set(nums2)
        # return a.intersection(b)
        m = max(*nums1,*nums2)
        d = [None]*(m+1)
        res= []
        for i in nums1:
            d[i] = False
        # print(d)
        for i in nums2:
            if d[i]==False:
                d[i] = True
        for i in range(0,m+1):
            if d[i]:
                res.append(i)
        return res