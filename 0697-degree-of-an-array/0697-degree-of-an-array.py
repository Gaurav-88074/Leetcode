class Solution:
    def findShortestSubArray(self, nums: List[int]) -> int:
        c = Counter(nums)
        arr = c.values()
        s = set()
        m = max(arr)
        for i in c:
            if c[i]==m:
                s.add(i)
        start = defaultdict(int)
        end   = defaultdict(int)
        for i,v in enumerate(nums):
            if v in s and v not in start:
                start[v] =i
            if v in s:
                end[v]=i
        res = float('inf')
        for i in s:
            res = min(res,end[i]-start[i]+1)
        return res