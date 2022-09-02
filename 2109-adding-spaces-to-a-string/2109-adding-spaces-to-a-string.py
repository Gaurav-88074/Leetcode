class Solution:
    def addSpaces(self, s: str, spaces: List[int]) -> str:
        res = [0]*(len(s)+len(spaces))
        ex= 0
        for i in spaces:
            res[i+ex] = " "
            ex+=1
        i = 0
        index=0
        for i in range(len(res)):
            if res[i]==0:
                res[i] = s[index]
                index+=1
        return "".join(res)