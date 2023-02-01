class Solution:
    def gcdOfStrings(self, str1: str, str2: str) -> str:
        def HCF(a,b):
            if b==0:return a
            return HCF(b,a%b)
        
        if str1+str2!=str2+str1:
            return ""
        
        hcf = HCF(len(str1),len(str2))
        
        return str2[:hcf]