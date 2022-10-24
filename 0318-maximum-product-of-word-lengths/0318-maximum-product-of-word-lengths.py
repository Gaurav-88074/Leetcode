class Solution:
    def maxProduct(self, words: List[str]) -> int:
        n = len(words)
        res = 0
        mask = [set(list(ww)) for ww in words]
        for i in range(n):
            a = words[i]
            for j in range(n):
                if i!=j:
                    b = words[j]
                    sa = mask[i]
                    sb = mask[j]
                    # if len(sa.intersection(sb))==0:
                    #     res = max(len(a)*len(b),res)
                    if not (sa & sb):
                        res = max(len(a)*len(b),res)
        return res
                    