class Solution:
    def search(self, nums: List[int], target: int) -> bool:
        pivot=[None]
        ans=[None]
        def binarySearch(nums,low,high):
            if low>high:
                return False
            mid = (low+high)//2
            if nums[mid]==target:
                return True
            elif target<nums[mid]:
                return binarySearch(nums,low,mid-1)
            else:
                return binarySearch(nums,mid+1,high)
        def valueSearch(nums,target,low,high):
            while low<=high:
                mid=(low+high)//2
                if mid-1>=0 and nums[mid]<nums[mid-1]:
                    pivot[0]=mid
                    # print("mil gya")
                    return True
                if(nums[mid]==target):
                    ans[0]=True
                    return True
                elif nums[mid]<nums[0]:
                    high=mid-1
                elif nums[mid]>nums[0]:
                    low=mid+1
                else:
                    left = valueSearch(nums,target,low,mid-1)   
                    right = valueSearch(nums,target,mid+1,high)
                    return left or right
            return False
        
        pivotSearch = valueSearch(nums,target,0,len(nums)-1)
        
        if ans[0]!=None:return ans[0]
        
        if pivot[0]!=None:
            left = binarySearch(nums,0,pivot[0]-1)
            right = binarySearch(nums,pivot[0],len(nums)-1)
            return left or right
        return target==nums[0]
                