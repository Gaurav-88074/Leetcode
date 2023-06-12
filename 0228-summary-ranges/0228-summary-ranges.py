class Solution:
    def summaryRanges(self, nums: List[int]) -> List[str]:
        res = []
        if not nums : return nums
        start = nums[0]
        pre = start
        for i in range(1,len(nums)):
            v=nums[i]
            if v==pre+1:
                # pre+=1
                pass
            else:
                if nums[i-1]-start ==0:
                    res.append(f"{start}")
                else:
                    res.append(f"{start}->{nums[i-1]}")
                start = v
            pre = v
        i = len(nums)
        if nums[i-1]-start ==0:
            res.append(f"{start}")
        else:
            res.append(f"{start}->{nums[i-1]}")
        return res