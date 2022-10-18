class Solution:
    def checkIfCanBreak(self, s1: str, s2: str) -> bool:
        s1 = list(s1)
        s2 = list(s2)
        s1.sort()
        s2.sort()
        flag = True
        for i in range(len(s1)):
            if s1[i]>s2[i]:
                flag = False
                break
        if flag:
            return flag
        for i in range(len(s1)):
            if s1[i]<s2[i]:
                return False
        return True