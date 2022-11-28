class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        looser = defaultdict(int)
        
        s1 = set()
        s2 = set()
        mx = -1
        for win,lose in matches:
            looser[lose]+=1
            s1.add(win)
            s2.add(lose)
        for i in s2:
            if i in s1:
                s1.remove(i)
        res1 = list(s1)
        res2 = []
        
        for i in looser:
            if looser[i]==1:
                res2.append(i)
        res1.sort()
        res2.sort()
        return [
            res1,
            res2
        ]