class Solution:
    def numberOfSubarrays(self, nums: List[int], k: int) -> int:
        res = 0
        pre = 0
        countOdd = 0
        d = defaultdict(int)
        d[k]=1
        for i,v in enumerate(nums):
            if (v&1)==1:
                countOdd+=1
            res+=d[countOdd]
            d[countOdd+k]+=1
        return res