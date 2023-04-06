class Solution:
    def findMaxLength(self, nums: List[int]) -> int:
        d =  dict()
        sum = 0
        res = 0
        d[0] =-1
        for index,i in enumerate(nums):
            # print(index,i)
            sum+=1 if i==1 else -1
            #-------------------------
            if sum in d :
                res = max(res,index - d[sum])
            else:
                d[sum] = index
        # print(d)
        
        return res; 