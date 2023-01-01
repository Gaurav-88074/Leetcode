class Solution:
    def countDigits(self, num: int) -> int:
        res = 0
        val = num
        for i in str(num):
            if int(i)==1 or num%int(i)==0:res+=1
        return res