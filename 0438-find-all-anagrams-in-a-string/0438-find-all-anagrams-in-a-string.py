class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        res = []
        if len(s)<len(p):
            return res
        def isPossible(c,target):
            for i in target:
                if c[i]<target[i]:
                    return False
            return True
        target = Counter(p)
        c = defaultdict(int)
        for i in range(0,len(p)):
            char=s[i]
            c[char]+=1
        index = 0
        
        if isPossible(c,target):
            res.append(index)
            
        for i in range(len(p),len(s)):
            char = s[index]
            c[char]-=1
            index+=1
            
            char = s[i]
            c[char]+=1
            
            if isPossible(c,target):
                res.append(index)
        return res
            
            
            