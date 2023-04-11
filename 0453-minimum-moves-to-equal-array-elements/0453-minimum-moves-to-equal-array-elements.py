from sortedcontainers import SortedList
class Solution:
    def minMoves(self, nums: List[int]) -> int:
        res = 0
        # l  = SortedList(nums,key = lambda x : -x)
        
        # while l[0]!=l[-1]:
        #     mn = l[-1]
        #     l.remove(mn)
        #     mn-=1
        #     l.add(mn)
        #     res+=1
        # return res

        mn = min(nums)
        for i in nums:
            res+=(i-mn)
        return res