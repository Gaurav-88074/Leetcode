class Solution(object):
    def destroyTargets(self, nums, space):
        d = defaultdict(list)
        for i in nums:
            mod = i%space
            d[mod].append(i)
        res = float('inf')
        gc = 0
        for i in d:
            d[i].sort()
            if len(d[i])>gc:
                res = d[i][0]
                gc = len(d[i])
            if len(d[i])==gc and d[i][0]<res:
                res = d[i][0]
                gc = len(d[i])
        return res
        
        