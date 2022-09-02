class Solution:
    def minimumCardPickup(self, cards: List[int]) -> int:
        d = dict()
        res = 100001
        
        for i in range(len(cards)):
            if cards[i] in d:
                res = min(res,i-d[cards[i]]+1)
            d[cards[i]] = i
        if res==100001:
            return -1
        return res
        