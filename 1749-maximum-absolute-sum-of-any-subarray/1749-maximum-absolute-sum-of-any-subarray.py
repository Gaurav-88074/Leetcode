class Solution:
    def maxAbsoluteSum(self, nums: List[int]) -> int:
        
        res1 = float('-inf')
        
        #----------------------
        value = 0
        for i in nums:
            value+=i
            if value>=0:
                res1 = max(res1, value)
            else:
                value = 0
        #---------------------------
        res2 = float('inf')
        value = 0
        for i in nums:
            value+=i
            if value<=0:
                res2 = min(res2, value)
            else:
                value = 0
        #------------------------
        res2 = abs(res2)
        #------------------------
    
        problem = [float('inf'),float('-inf')]
        if res1  in problem:
            return res2
        if res2 in problem:
            return res1
        return max(res1,res2)
                
        
        