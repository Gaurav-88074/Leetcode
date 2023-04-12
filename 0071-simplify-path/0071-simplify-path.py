class Solution:
    def simplifyPath(self, path: str) -> str:
        stack = []
        
        i = 0
        n = len(path)
        
        while i<n:
            if path[i]=="/":
                i+=1
                continue
            temp = ""
            while i < n and path[i]!="/":
                temp+=path[i]
                i+=1
            if temp==".":
                continue
            # print("temp ",temp)
            if temp==".." and stack:
                stack.pop()
            elif not stack and temp=="..":
                pass
            else:
                stack.append(temp)
            i+=1
        # print(stack)
        if not stack:
            return "/"
        return "/" + "/".join(stack)