class Solution:
    def commonChars(self, words: List[str]) -> List[str]:
        # def counter(w):
        #     d =defaultdict(int)
        #     for i in w:
        #         d[i]+=1
        #     return d
        # word=[]
        # res=[]
        # for i in words:
        #     word.append(counter(i))
        # for i in range(ord('a'),ord('z')+1):
        #     c = chr(i)
        #     v = float('inf')
        #     for x in word:
        #         v = min(v,x[c])
        #     if v>0:
        #         for ii in range(v):
        #             res.append(c)
        #     # res.append([c,v])
        # # print(res)
        # return res
        A = words
        res = Counter(A[0])
        for a in A:
            res &= Counter(a)
        return list(res.elements())