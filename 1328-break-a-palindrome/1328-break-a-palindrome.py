class Solution:
    def breakPalindrome(self, palindrome: str) -> str:
        if len(palindrome)==1:
            return ""
        s = list(palindrome)
        flag =0
        
        for i in range(len(s)//2):
            if s[i]!="a":
                s[i] = "a"
                
                flag=1
                break
        if flag==0:
            s[-1] =chr(ord(s[-1]) + 1)
        return "".join(s)