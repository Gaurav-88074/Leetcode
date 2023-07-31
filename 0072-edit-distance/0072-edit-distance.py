class Solution:
    def minDistance(self, word1: str, word2: str) -> int:
        s1  = word1
        s2  = word2

        @lru_cache(None)
        def compute(i,j):
            #---------------------------
            if i==-1 or j==-1:
                return j+1 if i==-1 else i+1
            #---------------------------
            #----------------------------
            if s1[i]==s2[j]:
                return compute(i-1,j-1)#no need to do something
            else:
                insert = 1 + compute(i,j-1)
                delete = 1 + compute(i-1,j)
                replace= 1 + compute(i-1,j-1)
                return min(insert,delete,replace)
            #------------------------------
        res = compute(len(s1)-1,len(s2)-1)
        return res
            
        