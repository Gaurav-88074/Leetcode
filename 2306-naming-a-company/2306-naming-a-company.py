class Solution:
    def distinctNames(self, ideas):
        count = defaultdict(set)
        for a in ideas:
            count[a[0]].add((a[1:]))
        res = 0
        # print(count.items())
        for a, seta in count.items():
            for b, setb in count.items():
                if a == b: continue
                same = len(seta & setb)
                res += (len(seta) - same) * (len(setb) - same)
        return res 