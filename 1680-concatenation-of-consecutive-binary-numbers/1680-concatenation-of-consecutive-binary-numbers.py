class Solution:
    def concatenatedBinary(self, n: int) -> int:
        output = 0
        mod = 10**9 + 7
        for x in range(1, n+1):
            output <<= x.bit_length()
            output |= x
            
            # output %= 10**9 + 7
            output%=mod
        return output%mod
        # return int(''.join(format(x,"b") for x in range(1, n+1)), 2) % 1_000_000_007
        