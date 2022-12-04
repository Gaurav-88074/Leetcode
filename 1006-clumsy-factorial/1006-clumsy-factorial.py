class Solution:
    def clumsy(self, n: int) -> int:
        stack = []
        p= 0
        arr=['*','/','+','-']
        stack.append(n)
        for i in range(n-1,0,-1):
            op = arr[p]
            p+=1
            p%=4
            
            if op=='*':
                stack.append(stack.pop() * i)
            elif op=='/':
                stack.append(stack.pop() // i)
            else:
                stack.append(op)
                stack.append(i)
        # print(stack)
        arr = stack
        stack = []
        for i in arr:
            if i!='+' and i!='-' and len(stack)!=0:
                op = stack.pop()
                value = stack.pop()
                if op=='+':
                    stack.append(value + i)
                else:
                    stack.append(value - i)
            else:
                stack.append(i)
                
        return stack[-1]