class Solution:
    def longestBeautifulSubstring(self, word: str) -> int:
        def getStack():
            return ['u', 'o', 'i', 'e', 'a']
        d = {
            'a':'e',
            'e':'i',
            'i':'o',
            'o':'u',
            'u':'u'
        }
        stack = getStack();
        res = 0
        c = 0
        
        for i,v in enumerate(word):
            if v==stack[-1]:
                c+=1
            elif v==d[stack[-1]] and c!=0:
                c+=1
                stack.pop()
            elif v!=stack[-1] and stack[-1]=="u":
                # print(word[i-c:i+1])
                res = max(res,c)
                if v=='a':c = 1
                else:     c = 0
                stack = getStack()
            else:
                # print(word[i-c:i+1],"discarded",i)
                if v=='a':c = 1
                else:     c = 0
                stack = getStack()
        if word[-1]=='u' and stack[-1]=="u":
            res = max(res,c)
        
        return res