class Solution(object):
    def isValid(self, s):
        if len(s)<3:return False
        
        stack = []
        for i in s:
            stack.append(i)
            # print(stack)
            if len(stack)>=3 and stack[-3]=="a" and stack[-2]=="b" and stack[-1]=="c":
                stack.pop()
                stack.pop()
                stack.pop()
        return len(stack)==0
        