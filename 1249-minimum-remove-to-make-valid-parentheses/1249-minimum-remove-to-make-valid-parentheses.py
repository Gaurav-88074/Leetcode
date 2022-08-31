class Solution:
    def minRemoveToMakeValid(self, s: str) -> str:
        stack = []
        for i in range(len(s)):
            if s[i]==")" and len(stack)!=0 and stack[-1][1]=="(":
                stack.pop()
                continue
            if s[i] in ["(",")"]:
                stack.append(
                    [i,s[i]]
                )
        # print(stack)
        st = set()
        for i in stack:
            st.add(i[0])
            
        res = []
        for i in range(len(s)):
            if i not in st:
                res.append(s[i])
        return "".join(res)
            