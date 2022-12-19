class Solution:
    def countSubarrays(self, nums: List[int], k: int) -> int:
        index = 0
        res = 0
        summ = 0
        for i,v in enumerate(nums):
            summ+=v
            while (summ * (i-index+1)) >=k:
                summ-=nums[index]
                index+=1
            n=(i-index+1)
            # print(nums[index:index+n])
            # res += ((n * (n-1))//2)
            res+=n
        return res
                 