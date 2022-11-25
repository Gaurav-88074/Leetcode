class Solution:
    def addToArrayForm(self, num: List[int], k: int) -> List[int]:
        num = list(map(str,num))
        
        value = "".join(num)
        
        value = int(value)
        
        res = value + k
        
        res = str(res)
        
        res = list(res)
        
        res = list(map(int,res))
        
        return res