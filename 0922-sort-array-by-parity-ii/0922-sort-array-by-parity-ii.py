class Solution:
    def sortArrayByParityII(self, nums: List[int]) -> List[int]:
        
        nums.sort(key = lambda x : x%2!=0)
        evenIndex = 1
        # print(nums)
        for i in range(len(nums)-2,-1,-2):
            if evenIndex>=len(nums)//2:break
            # print("at",i)
            # a = nums[i]
            # b = nums[evenIndex]
            nums[i],nums[evenIndex] = nums[evenIndex],nums[i]
            evenIndex+=2
            # print(nums)
            
        return nums