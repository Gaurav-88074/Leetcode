class Solution(object):
    def gcdOfStrings(self, str1, str2):
        
        for i in range(len(str2)):
            sub = str2[ : len(str2) - i]
            
            a = str1.count(sub)
            b = str2.count(sub)
            
            if a * len(sub)!=len(str1) or b * len(sub)!=len(str2):
                continue
            return sub
            
        return ""
        