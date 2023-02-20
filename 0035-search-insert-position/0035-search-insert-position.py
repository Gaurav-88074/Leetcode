class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        low = 0
        high = len(nums)-1
        
        while low<=high:
            mid = (low+high)//2
            # if(low==high):
            #     break
            if(nums[mid]==target):
                return mid;
            else:
                if target<nums[mid]:
                    high = mid - 1
                else:
                    low  = mid + 1
        return high + 1
        