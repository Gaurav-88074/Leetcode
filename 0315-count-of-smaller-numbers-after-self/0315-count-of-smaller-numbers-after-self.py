from sortedcontainers import SortedList
class Solution:
    def countSmaller(self, nums: List[int]) -> List[int]:
        l = SortedList()
        res = [0]*len(nums)
        i = len(nums)-1
        for x in range(len(nums)-1,-1,-1):
            value = nums[x]
            bi = l.bisect_left(value)
            # print(bi,len(l)==bi)
            # if len(l)==bi:
            #     res[x] = 0
            # else:
            res[x] = bi
            l.add(value)
            # print(l)
        return res