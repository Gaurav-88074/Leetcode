from sortedcontainers import SortedList
class Solution:
    def countFairPairs(self, nums: List[int], lower: int, upper: int) -> int:
        #code written by gaurav
        nums.sort()
        i = 0
        j = len(nums)-1
        res = 0
        while i<j:
            s = nums[i] + nums[j]
            if s>=lower and s<=upper:
                l = SortedList(nums[i : j+1])
                while l:
                    # print(l)
                    a = l[0]
                    
                    value = lower-a
                    left = l.bisect_left(lower-a)
                    right= l.bisect_right(upper-a)
                    # print(l,left,right,"diff =",abs(left-right))
                    if lower - a <= a <= upper - a:
                        # print(lower-a,a,upper-a)
                        res -= 1
                    res+=abs(left-right)
                    
                    l.remove(a)
                return res      
            if s<lower:
                i+=1
            if s>upper:
                j-=1
        return 0