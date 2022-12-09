class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[k]=1
        res = 0
        p = 0
        for i in nums:
            p+=i
            # mod = p%k
            
            res += d[p]
            d[p+k]+=1
        # print(d)
        return res