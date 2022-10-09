class Solution:
    def findArray(self, pref: List[int]) -> List[int]:
        v = pref[0]
        res = [v]
        xor = v
        
        txor =v
        for i in range(1,len(pref)):
            value = pref[i]
            xor^=value
            res.append(xor)
            txor^=xor
            xor = txor
        return res
            