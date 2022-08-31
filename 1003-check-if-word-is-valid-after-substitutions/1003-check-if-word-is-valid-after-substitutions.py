class Solution:
    def isValid(self, s: str) -> bool:
        if len(s)<3:return False
        
        stack = []
        for i in s:
            stack.append(i)
            # print(stack)
            if len(stack)>=3 and stack[-3]+stack[-2]+stack[-1]=="abc":
                stack.pop()
                stack.pop()
                stack.pop()
        return len(stack)==0
            