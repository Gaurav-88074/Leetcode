class Solution:
    def validateStackSequences(self, pushed: List[int], popped: List[int]) -> bool:
        stack=[]
        j=0
        n=len(pushed)
        for i in pushed:
            stack.append(i)
            while stack and j<n and stack[-1]==popped[j]:
                stack.pop()
                j+=1
        return not stack