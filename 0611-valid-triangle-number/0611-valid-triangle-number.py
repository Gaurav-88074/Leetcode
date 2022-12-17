class Solution(object):
    def triangleNumber(self, nums):
        res = [0]
        def compute(nums,value,left,right,res):
            # print("-----------")
            # print(left,right)
            while(left<right): 
                s = (nums[left]+nums[right])
                if value<s:
                    res[0]+=(right-left)
                    left+=1
                else:
                    right-=1
            # print(right-left)
            # res[0]+=(right-left)
        nums.sort(reverse=True)
        last = len(nums)-2
        for i in range(0,last):
            compute(nums,nums[i],i+1,len(nums)-1,res)
        return res[0]
        