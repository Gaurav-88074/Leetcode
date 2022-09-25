class Solution:
    def longestSubarray(self, nums: List[int]) -> int:
        count=0
        prev= max(nums)
        arr  =[]
        for i in nums:
            if i==prev: count+=1
            else:
                arr.append(count)
                count=0
        arr.append(count)
        if len(arr)==0 or max(arr)==0:return 1
        return max(arr)