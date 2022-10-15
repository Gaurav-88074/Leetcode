class Solution:
    def productQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        v = 1
        mod  = 10**9 + 7
        power = []
        while v<=n:
            v = v<<1
        v = v>>1
        # print(v)
        powers = []
        while n>0 : 
            if n>=v:
                n-=v
                powers.append(v)
                v = v>>1
            else:
                v = v>>1
        # print(powers)
        powers.reverse()
        pre = 1
        prefix= []
        for i in powers:
            pre*=i
            prefix.append(pre)
        # print(prefix)
        res = []
        for a,b in queries:
            if a==0:
                res.append(prefix[b]%mod)
            else:
                res.append((prefix[b]//prefix[a-1])%mod)
        return res