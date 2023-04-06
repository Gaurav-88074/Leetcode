from itertools import *
class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        # nums = [*nums]
        l = list(accumulate(nums))
        r = list(accumulate(nums[::-1]))
        r = r[::-1]
        print(l)
        print(r)
        # if r[1]==0:
        #     return 0
        # if l[-2]==0:
            # return len(nums)-1
        for i in range(len(nums)):
            if l[i]==r[i]:
                return i
        return -1