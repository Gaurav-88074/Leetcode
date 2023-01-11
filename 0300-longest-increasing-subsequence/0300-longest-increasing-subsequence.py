class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        temp = []
        temp.append(nums[0])
        for i in range(1,len(nums)):
            if nums[i]>temp[-1]:
                temp.append(nums[i])
            else:
                index = bisect.bisect(temp,nums[i]-1)
                temp[index]=nums[i]
            # print(temp)
        return len(temp)
            