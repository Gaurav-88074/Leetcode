class Solution:
    def calculate(self, s):
        # s = list(s)
        # print(s)
        def add(stack,v):
            stack.pop()
            left = stack.pop()
            right= v
            res = left+right
            
            if  len(stack)!=0 and stack[-1]=='+':
                add(stack,res)
            elif len(stack)!=0 and stack[-1]=="-":
                sub(stack,res)
            else:
                stack.append(res)
            
        def sub(stack,v):
            if ( len(stack)==1 or (len(stack)>=2 and stack[-2]=='(')) :
                    if len(stack)==1:
                        stack.pop()
                    elif len(stack)>=2:
                        stack.pop()
                        # stack.pop()
                    
                    if  len(stack)!=0 and stack[-1]=='+':
                        add(stack,-v)
                    elif len(stack)!=0 and stack[-1]=="-":
                        sub(stack,-v)
                    else:
                        stack.append(-v)
            
            else:
                stack.pop()
                left = stack.pop()
                right= v
                res = left - right

                if  len(stack)!=0 and stack[-1]=='+':
                    add(stack,res)
                elif len(stack)!=0 and stack[-1]=="-":
                    sub(stack,res)
                else:
                    stack.append(res)
            
        stack = []
        index = 0
        while index<len(s):
            
            v = ord(s[index])
            if v==32:
                index+=1
                continue
                
            if v>=48 and v<=57:
                value = 0
                while index<len(s) and ord(s[index])>=48 and ord(s[index])<=57:
                    value*=10
                    ac = ord(s[index])-48
                    value+=ac
                    index+=1
                
                if  len(stack)!=0 and stack[-1]=='+':
                    add(stack,value)
                elif len(stack)!=0 and stack[-1]=="-":
                    sub(stack,value)
                else:
                    stack.append(value)
                continue
                                                          
                #number
            elif v==43 or v==45:
                stack.append(s[index])
            elif s[index]=='(':
                
                stack.append(s[index])
            elif s[index]==')':
                
                value = stack.pop()
                stack.pop()
            
                if  len(stack)!=0 and stack[-1]=='+':
                    add(stack,value)
                elif len(stack)!=0 and stack[-1]=="-":
                    sub(stack,value)
                else:
                    # stack.pop()
                    stack.append(value)
        
            index+=1

        return stack[-1]
        # return 2