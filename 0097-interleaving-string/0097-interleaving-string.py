class Solution:
    @lru_cache(None)
    def check(self,index,p1,p2):
        
        #------------------
        s1 = self.s1 
        s2 = self.s2 
        s3 = self.s3 
        #--------------------
        if index==len(s3):  
            return True
        
        if p1==len(s1) and p2==len(s2): 
            return False
        
        if p1==len(s1):
            return (s2[p2] == s3[index])  and self.check(index+1,p1,p2+1)
        
        if p2==len(s2):
            return (s1[p1] == s3[index])  and self.check(index+1,p1+1,p2)
        
        
        
        case1 =  (s1[p1] == s3[index]) and self.check(index+1,p1+1,p2)
        case2 =  (s2[p2] == s3[index]) and self.check(index+1,p1,p2+1)
        
        
        return case1 or case2;
        
        
    def isInterleave(self, s1: str, s2: str, s3: str) -> bool:
        self.s1 = s1
        self.s2 = s2
        self.s3 = s3
        return len(s1)+len(s2)==len(s3) and self.check(0,0,0);