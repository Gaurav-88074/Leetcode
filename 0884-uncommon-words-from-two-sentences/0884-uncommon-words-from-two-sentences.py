class Solution:
    def uncommonFromSentences(self, s1: str, s2: str) -> List[str]:
        
        res = set()
        discarded = set()
        for i in s1.split(" "):
            if i in res:
                res.remove(i)
                discarded.add(i)
            elif i in discarded:
                continue
            else:
                res.add(i)
        for i in s2.split(" "):
            if i in res:
                res.remove(i)
                discarded.add(i)
            elif i in discarded:
                continue
            else:
                res.add(i)
        return res
                