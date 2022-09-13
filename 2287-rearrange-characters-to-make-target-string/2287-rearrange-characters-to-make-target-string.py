from typing import Counter
class Solution:
    def rearrangeCharacters(self, s: str, target: str) -> int:
        c = Counter(s)
        v = Counter(target)
        res = 0
        while True:
            for i in v:
                count = v[i]
                if c[i]<count : return res
                else : c[i]-=count
            res+=1
        return res