class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        def s(n) :
            Primes = [0] * (10**6 +1)
            Primes[0] = 1
            i = 3
            while(i*i <= n) :
                if (Primes[i // 2] == 0) :
                    for j in range(3 * i, n+1, 2 * i) :
                        Primes[j // 2] = 1

                i += 2
            return Primes
        p = s(right+1)
        res = []
        
        for i in range(left,right+1):
            if (i == 2) :
                res.append(i)
            elif (i % 2 == 1 and p[i // 2] == 0) :
                res.append(i)
        mn  =float('inf')
        v=[-1,-1]
        for i in range(1,len(res)):
            if res[i]-res[i-1]<mn:
                mn = res[i]-res[i-1]
                v=[res[i-1] , res[i]]
        return v
        