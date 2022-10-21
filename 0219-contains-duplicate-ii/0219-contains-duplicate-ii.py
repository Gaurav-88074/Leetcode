class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        d = defaultdict(list)
        if k==0:return False
        for i in range(len(nums)):
            v = d[nums[i]]
            v.append(i)
            if len(v)>=2 and abs(v[-1]-v[-2])<=k:
                return True
        return False