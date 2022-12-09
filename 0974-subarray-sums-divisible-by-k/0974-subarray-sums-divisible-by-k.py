class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        d = defaultdict(int)
        d[0]+=1
        p=0
        res = 0
        for i in nums:
            p+=i
            mod = p%k
            print(mod,d[mod])
            res += d[mod]
            d[mod]+=1
        # print(d)
        return res
        