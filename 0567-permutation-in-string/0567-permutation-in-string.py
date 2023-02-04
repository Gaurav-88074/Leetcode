class Solution:
    def check(self,d,that):
        for i in range(26):
            if(d[i]!=that[i]):return False
        return True;
    def checkInclusion(self, s1: str, s2: str) -> bool:
        if(len(s1)>len(s2)) : return False
        
        d = [0] * 26
        for i in s1:
            d[ord(i)-97]+=1
        # print(d)
        #---------------
        that = [0] * 26
        for i in range(len(s1)-1):
            that[ord(s2[i])-97]+=1;
        # res = False
        start = 0
        for i in range(len(s1)-1,len(s2)):
            # print("window size : ",start,i)
            that[ord(s2[i])-97]+=1
            res = self.check(d,that)
            if res==True : return True
            
            that[ord(s2[start])-97]-=1
            start+=1
        return False