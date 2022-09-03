class Solution(object):
    
    def generate(self,n,b,open,close,i,l):
        if i == 2*n :
            # print(b)
            l.append(b)
            return
        if open<n:
            self.generate(n, b+"(", open+1, close,i+1,l)
        if open>close:
            self.generate(n, b+")", open, close+1,i+1,l)
    def generateParenthesis(self, n):
        res = []
        self.generate(n,"",0,0,0,res)
        return res
        
        