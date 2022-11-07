class Solution(object):
    def maximum69Number (self, num):
        stack = []
        d = 1
        while num>0:
            value = num%10
            stack.append(value)
            div = 10*d
            num//=div
        # print(stack)
        flag = 1
        while len(stack)!=0:
            value = stack.pop()
            if value==6 and flag ==1:
                value = 9
                flag=0
            num +=value
            
            num*=10
        num//=10
        return num
        """
        :type num: int
        :rtype: int
        """
        