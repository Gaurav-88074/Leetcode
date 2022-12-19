class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        zero=0
        one=0
        index = 0
        res = 0
        
        for i,v in enumerate(nums):
            if v==1:
                one+=1
            else:
                zero+=1
            # mn = min(one,zero)
            while zero>k :
                ch = nums[index]
                index+=1
                
                if ch==1:one-=1
                else:zero-=1
                
                zero = zero
            # print(nums[index:i+1])
            res = max(res,i-index+1)
        return res