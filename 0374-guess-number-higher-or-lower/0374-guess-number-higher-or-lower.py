# The guess API is already defined for you.
# @param num, your guess
# @return -1 if num is higher than the picked number
#          1 if num is lower than the picked number
#          otherwise return 0
# def guess(num: int) -> int:

class Solution:
    def guessNumber(self, n: int) -> int:
        
        def compute(start,end):
            mid = start + (end-start)//2
            # print("-------------")
            # print(start,end)
            # print(mid)
            v = guess(mid)
            
            if(v==0):
                return mid
            elif v==-1:
                # print("going left")
                return compute(start,mid-1)
            else:
                # print("going right")
                return compute(mid+1,end)
        return compute(1,n)  