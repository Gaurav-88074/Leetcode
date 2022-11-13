class Solution:
    def subarrayLCM(self, nums: List[int], k: int) -> int:
        def LCM(a,b):
            if a%b==0 or b%a ==0 : 
                return max(a,b)
            else:
                return a*b
        res= 0
        for i in range(0,len(nums)):
            lcm =1
            for j in range(i,len(nums)):
                lcm = LCM(lcm,nums[j])
                if lcm==k:
                    # print(i,j)
                    res+=1
                # else:
                #     break
        return res