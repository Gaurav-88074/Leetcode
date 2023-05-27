class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> List[str]:
        
        d = set(wordDict)
        res = []
        l = []
        def compute(x):
            if x == len(s):
                res.append(" ".join(l))
                return 
    
            for i in range(x, len(s)):
                if s[x:i+1] in d:
                    l.append(s[x:i+1])
                    compute(i + 1)
                    l.pop()
                
            

        compute(0)
        return res