class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        pre = 0
        s = 0
        res = float('inf')
        for i in range(len(nums)):
            s+=nums[i]
            while s>=target:
                res = min(res,i-pre+1)
                s-=nums[pre]
                pre+=1
                    
                         
                            
        if res==float('inf'):
            return 0
        if res==0:return 1
        return res
            
                
            
            