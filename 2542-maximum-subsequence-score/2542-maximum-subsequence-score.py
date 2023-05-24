from sortedcontainers import SortedList, SortedDict,SortedSet
class Solution:
    def maxScore(self, nums1: List[int], nums2: List[int], k: int) -> int:
        
        arr = []
        for i in range(len(nums1)):
            arr.append([
                nums1[i],nums2[i]
            ])
        arr.sort(key = lambda x :  (-x[1]))
        res = 0
        # print(arr)
        value = 0
        minheap = SortedList()
        for i in range(len(arr)):
            a,b = arr[i]
            value+=a
            minheap.add(a)
            if i>=(k-1):
                res = max(res ,value * b)
                value-= minheap.pop(0)
                  
        return res