class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        # d = defaultdict(list)
        # if k==0:return False
        # for i in range(len(nums)):
        #     v = d[nums[i]]
        #     v.append(i)
        #     if len(v)>=2 and abs(v[-1]-v[-2])<=k:
        #         return True
        # return False
        dic = {}
        for i in range(len(nums)):
            if nums[i] not in dic:
                dic[nums[i]] = i
            else:
                if i - dic[nums[i]] <= k:
                    return True
                dic[nums[i]] = i
        return False