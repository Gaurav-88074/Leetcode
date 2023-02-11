class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        
        d=dict()
        stack = [-1]
        for i in nums2[::-1]:
            v = i
            while stack[-1]!=-1 and stack[-1]<i:
                stack.pop()
            d[v] = stack[-1]
            stack.append(v)
        res = []
        for i in nums1:
            res.append(d[i])
        return res