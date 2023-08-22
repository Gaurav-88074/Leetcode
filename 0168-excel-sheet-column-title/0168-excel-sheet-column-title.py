class Solution:
    def convertToTitle(self, columnNumber: int) -> str:
        res = []
        
        n = columnNumber
        nums  =[]
        def compute(n):
            if n<=26:
                char =  n
                nums.append(chr(64+char))
                return 
            char =  n%26
            if char==0:
                nums.append('Z')
                n-=1
            else:
                nums.append(chr(64+char))
            n-=char
            n//=26
            compute(n)
        compute(n)
        # print(list(reversed(nums)))
        return "".join(list(reversed(nums)))
            
            