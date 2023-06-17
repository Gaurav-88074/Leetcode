class Solution(object):
    def bitwiseComplement(self, n):
        if n==0 or n==1 : return n^1
        answer = 0
        pos = 0
        
        while n>0:
            if (n&1)==1:
                mask = 0
                mask<<=pos
                answer=answer|mask
            else:
                mask = 1
                mask<<=pos
                answer=answer|mask
            pos+=1
            n>>=1
        return answer