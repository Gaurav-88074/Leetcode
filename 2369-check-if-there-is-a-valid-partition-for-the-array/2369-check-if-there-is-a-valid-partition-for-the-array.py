class Solution:
    def validPartition(self, nums: List[int]) -> bool:
        def op1(nums,index):
            if index+1>=len(nums) : return False
            return nums[index]==nums[index+1]
        def op2(nums,index):
            if index+2>=len(nums) : return False
            return nums[index]==nums[index+1]==nums[index+2]
        def op3(nums,index):
            if index+2>=len(nums) : return False
            return nums[index+2]-nums[index+1]==1 and nums[index+1] - nums[index]==1
        @lru_cache(None)
        def check(index):
            if index==len(nums):
                return True
            if op1(nums,index) and check(index+2):
                return True
            if op2(nums,index) and check(index+3):
                return True
                 
            if op3(nums,index) and check(index+3):
                return True
            
            return False
        
        # print(right)
        res =check(0)
        check.cache_clear()
        return res