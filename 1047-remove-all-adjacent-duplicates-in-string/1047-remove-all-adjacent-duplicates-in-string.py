class Solution:
    def removeDuplicates(self, s: str) -> str:
        stack = []
        for i in s:
            if len(stack)==0 or stack[-1]!=i:
                stack.append(i)
            else:
                while len(stack)!=0 and stack[-1]==i:
                    stack.pop()
        return "".join(stack)