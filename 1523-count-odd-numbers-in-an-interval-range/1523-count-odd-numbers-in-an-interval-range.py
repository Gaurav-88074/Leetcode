class Solution:
    def countOdds(self, low: int, high: int) -> int:
        a = 0
        low-=1
        if low%2==0:
            a = low//2
        else:
            a = (low+1)//2
        
        b = 0
        if high%2==0:
            b = high//2
        else:
            b = (high+1)//2
        # print(a,b)
        return b-a
        
            