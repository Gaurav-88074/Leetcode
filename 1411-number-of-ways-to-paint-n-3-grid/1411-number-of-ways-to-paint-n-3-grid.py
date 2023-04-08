class Solution:
    def numOfWays(self, n: int) -> int:
        c = [1,2,3]
        mod=10**9 + 7
        #==========================
        pair = []
        def gen(n,pre,temp):
            if len(temp)==3:
                pair.append([*temp])
                return
            for i in c:
                if pre!=i:
                    temp.append(i)
                    gen(n,i,temp)
                    temp.pop()
        #==================================
        @lru_cache(None)
        def compute(n,a,b,c):
            if n==0:
                return 1
            res = 0
            #-------------------
            for i,j,k in pair:
                if i!=a and j!=b and k!=c:
                    res+=compute(n-1,i,j,k)
            #-------------------
            res%=mod
            return res
        
        # return 
        gen(3,0,[])#use brain like Gaurav
        # print(pair)
        return compute(n,0,0,0)%mod