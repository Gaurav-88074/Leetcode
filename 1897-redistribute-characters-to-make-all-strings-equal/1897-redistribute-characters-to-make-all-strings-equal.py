class Solution:
    def makeEqual(self, words: List[str]) -> bool:
        d=defaultdict(int)
        for i in words:
            for j in i:
                d[j]+=1
        size = len(words)
        for i in d:
            if d[i]%size!=0:
                return False
        return True