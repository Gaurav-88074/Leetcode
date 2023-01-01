class Solution:
    def wordPattern(self, pattern: str, s: str) -> bool:
        s = s.split(" ")
        if len(s)!=len(pattern):return False
        
        d = dict()
        check =set()
        for i in range(len(pattern)):
            v = pattern[i]
            if v in d:
                if d[v]!=s[i]:
                    return False
            else:
                if s[i] in check:return False
                d[v] = s[i]
                check.add(s[i])
                
    
                
        return True