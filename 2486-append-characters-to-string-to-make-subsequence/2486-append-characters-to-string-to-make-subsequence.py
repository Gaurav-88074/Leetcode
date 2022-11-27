class Solution:
    def appendCharacters(self, s: str, t: str) -> int:
        p = 0
        for i in range(len(s)):
            if s[i]==t[p]:
                p+=1
            if p==len(t):
                return 0
        # print(p)
        return len(t)-p