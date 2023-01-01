class Solution:
    def minimumPartition(self, s: str, k: int) -> int:
        res = 0
        val = 0
        
        for i in s:
            if int(i)>k:return -1
            val+=int(i)
            if val>k:
                val-=int(i)
                val//=10
                # print(val)
                res+=1
                val = int(i)
            val*=10
        val//=10
        # print(val)
        if val<=k:
            res+=1
        return res
                