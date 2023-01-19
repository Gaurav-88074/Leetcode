class Solution:
    def removeDuplicates(self, s: str, k: int) -> str:
        stack = []
        for i,v in enumerate(s):
            if not stack:
                stack.append([v,1])
            elif stack[-1][0]==v:
                stack[-1][1]+=1
                if stack[-1][1]==k:
                    stack.pop()
            else:
                stack.append([v,1])
        # print(stack)
        res = ""
        for v,count in stack:
            res+=v*count
        return res
            