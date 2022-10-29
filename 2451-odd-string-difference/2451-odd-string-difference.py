class Solution:
    def oddString(self, words: List[str]) -> str:
        arr = []
        d = dict()
        for s in words:
            v = []
            for i in range(1,len(s)):
                v.append(str(ord(s[i])-ord(s[i-1])))
            arr.append(tuple(v))
            d[tuple(v)] = s
        # print(arr)
        c = Counter(arr)
        # print(d)
        for i in c:
            if c[i]==1:
                return d[i]
        return words[0]