class Solution:
    def entityParser(self, text: str) -> str:
        stack = []
        for i in text:
            stack.append(i)
            if len(stack)>=6:
                check = stack[-6]+stack[-5]+stack[-4]+stack[-3]+stack[-2]+stack[-1]
                if check=="&quot;":
                    for i in range(6):
                        stack.pop()
                    stack.append('"')
                    stack.append("None")
                elif check=="&apos;":
                    for i in range(6):
                        stack.pop()
                    stack.append("'")
                    stack.append("None")
            if len(stack)>=5:
                check = stack[-5]+stack[-4]+stack[-3]+stack[-2]+stack[-1]
                if check=="&amp;":
                    for i in range(5):
                        stack.pop()
                    stack.append('&')
                    stack.append("None")
            if len(stack)>=4:
                check = stack[-4]+stack[-3]+stack[-2]+stack[-1]
                if check=="&gt;":
                    for i in range(4):
                        stack.pop()
                    stack.append('>')
                    stack.append("None")
                if check=="&lt;":
                    for i in range(4):
                        stack.pop()
                    stack.append('<')
                    stack.append("None")
            if len(stack)>=7:
                check =stack[-7]+ stack[-6]+stack[-5]+stack[-4]+stack[-3]+stack[-2]+stack[-1]
                if check=="&frasl;":
                    for i in range(7):
                        stack.pop()
                    stack.append('/')
                    stack.append("None")
        res =[]
        for i in stack:
            if i!="None":res.append(i)
        return "".join(res)
                
            