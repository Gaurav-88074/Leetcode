class Solution:
    def countPairs(self, d: List[int]) -> int:
        mod = 10**9 + 7
        
        def getSum(n):
            v = n*(n-1)
            return v//2
        
        
        c = Counter(d)
        
        powers = [2**i for i in range(0,23)]
        st = set()
        res = 0
        
        for i in c.keys():
            if c[i]==0: continue
                
            freq = c[i]
            
            for power in powers:
                if power - i in c:
                    thatFreq = c[power - i]
                    if thatFreq==0 or (power-i==i): 
                        res+= getSum(freq)
                        res%=mod
                    else:
                        key = (power-i,i)
                        if not key in st:
                            st.add((i,power-i))
                            res += (freq*thatFreq)
                            res%=mod
                    
                    # print(i,power-i)
                    # c[i]-=m
                    # c[power-i]-=m
        # res//=2
        
        
        # for i in c.keys():
        #     freq = c[i]
        #     for power in powers:
        #         if power - i in c:
        #             thatFreq = c[power - i]
        #             if thatFreq==0 or (power-i==i): 
        #                 res+= getSum(freq)
        return res