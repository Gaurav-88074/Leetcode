from typing import Counter
class Solution:
    def topKFrequent(self, words: List[str], k: int) -> List[str]:
        d = dict(Counter(words))
        res = []
        for i in d:
            res.append([i,d[i]])
        res.sort(key = lambda x : (-x[1],x[0]))
        # print(res)
        v =[]
        for i in res:
            v.append(i[0])
            if len(v)==k:break
        return v