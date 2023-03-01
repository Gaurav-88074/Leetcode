class Solution:
    def findTheLongestSubstring(self, s: str) -> int:
        res = 0
        pre = 0
        
        v  = set(['a','e','i','o','u'])
        vi = { 
            'a':1,'e':2,
            'i':3,'o':4,
            'u':5
        }
        mask = 0
        d = defaultdict(int)
        d[0]=-1
        for i,c in enumerate(s):
            if c in v:
                bitmask = 1<<vi[c]
                mask^=bitmask
            #--------------------------------
            if mask in d:
                res =max(res,i - d[mask]) 
            else:
                d[mask] = i
            #---------------------------------
        return res