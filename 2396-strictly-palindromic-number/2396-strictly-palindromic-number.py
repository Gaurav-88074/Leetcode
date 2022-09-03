class Solution:
    def isStrictlyPalindromic(self, n: int) -> bool:
        def nb(n, b):
            if n == 0:
                return [0]
            digits = []
            while n:
                digits.append(int(n % b))
                n //= b
            return digits[::-1]
        for i in range(2,n-1):
            v = nb(n,i)
            if v!=v[::-1]:
                return False
        return True