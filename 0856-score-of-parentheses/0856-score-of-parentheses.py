class Solution:
    def scoreOfParentheses(self, s: str) -> int:
        stack = []
        res = 0
        temp=0
        for i,c in enumerate(s):
            if c=='(':
                score = 0
                stack.append([i,c,score])
            else:
                if stack and stack[-1][1]=='(':
                    node = stack.pop()
                    d = abs( i - node[0])
                    if d==1:
                        # res+=1
                        if stack:
                            stack[-1][2] += 1
                        else:
                            res+=1
                    else:
                        value = node[2]
                        # res-=value
                        
                        if stack:
                            stack[-1][2] += 2*value
                        else:
                            res+=(2 * value)
                        
                else:
                    stack.append([i,c,0])
            # print(stack)
            # print("res =",res)
        
        return res