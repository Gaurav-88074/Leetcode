class Solution:
    def canSplitArray(self, nums: List[int], m: int) -> bool:
        c= 0
        @lru_cache(None)
        def compute(a,b):
            # print(a,b)
            if a==b:
                return [True,nums[a],1]
            # if sum(nums[a:b])>=m:
            #     return [True,1]
            res = [False,0,0]
            
            for i in range(a,b):
                left ,val1,count1 = compute(a,i)
                right,val2,count2 = compute(i+1, b)
                if (count1==1 or val1>=m) and (count2==1 or val2>=m):
                    res = [True,val1+val2,count1+count2]
            return res
        # c+=res[1]
        res = compute(0,len(nums)-1)
        a,b,c=res
        # print(res)
        return a and c>=len(nums)