class Solution:
    def smallestDivisor(self, nums: List[int], threshold: int) -> int:
        res = max(nums)
        
        left = 1
        right= max(nums)
        
        while(left<=right):
            div =(left+right)//2
            s = sum(
                [
                    math.ceil((i)/div) for i in nums
                ]
            )
            
            if s>threshold:
                left=div+1
            else:
                res = min(res,div)
                right=div-1
        return res