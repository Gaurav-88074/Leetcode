class Solution:
    def minElements(self, nums: List[int], limit: int, goal: int) -> int:
        
        s = sum(nums)
        res = 0
        
        required = goal - s
        
        # print(required)
        while required!=0:
            # res+=1
            
            if abs(required)<=limit:
                res+=1
                required=0
            else:
                #just abs things\U0001f642
                #use brain
                if required<0:
                    div = abs(required)//limit
                    #---------
                    res+=div
                    #--------
                    required+=(limit*div)
                    # print("required",required,"res=",res,"div",div)
                else:
                    div = abs(required)//limit
                    #---------
                    res+=div
                    #---------
                    required-=(limit*div)
                    # print("required",required,"res=",res,"div",div)
        
        return res