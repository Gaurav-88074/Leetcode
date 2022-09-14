class Solution(object):
    def removeOccurrences(self, s, part):
        #using stack
        stack = []
        for i in s:
            stack.append(i)
            if len(stack)>=len(part) and "".join(stack[len(stack)-len(part):])==part:
                for i in range(len(part)):
                    stack.pop()
        
        return "".join(stack)
        