class Solution:
    def closetTarget(self, words: List[str], target: str, startIndex: int) -> int:
        r = [*words]
        # r.reverse()
        r = [*r,*words,*words]
        res =float('inf')
        i = startIndex+len(words)
        s=i
        while i>=0:
            if r[i]==target:
                res = min(res,abs(i-s))
            i-=1
        i = startIndex+len(words)
        while i<len(r):
            if r[i]==target:
                res = min(res,abs(i-s))
            i+=1
        # print(r)
        return res if res!=float('inf') else -1