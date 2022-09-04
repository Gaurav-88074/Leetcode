class Solution:
    def checkDistances(self, s: str, distance: List[int]) -> bool:
        d  =dict()
        for i in range(len(s)):
            if s[i] in d:
                d[s[i]].append(i)
            else:
                d[s[i]] = [i]
        # print(d)
        res  =dict()
        for i in d:
            a,b = d[i]
            res[i] = b-a-1
        # print(res)
        for i in res:
            value = res[i]
            index = ord(i)-97
            if distance[index]!=value:
                return False
        return True