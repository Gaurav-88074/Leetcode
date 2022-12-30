class Solution:
    def wiggleSort(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        """
        res = [0]*len(nums)
        j = 0
        nums.sort(reverse = True)
        # i = 1
        for i in range(1,len(nums),2):
            res[i] = nums[j]
            j+=1
        for i in range(0,len(nums),2):
            res[i] = nums[j]
            j+=1
        # print(res)
        for i in range(len(nums)):
            nums[i] = res[i]
        # return res
        