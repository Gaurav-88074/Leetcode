class Solution:
    def numJewelsInStones(self, jewels: str, stones: str) -> int:
        d = set(list(jewels))
        res = 0
        for i in stones:
            if i in d:
                res+=1
        return res