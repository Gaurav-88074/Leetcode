class Solution:
    def concatenatedBinary(self, n: int) -> int:
#         output = 0
#         mod = 10**9 + 7
#         for x in range(1, n+1):
#             output <<= x.bit_length()
#             output |= x
            
#             output %= 10**9 + 7
#         return output
        # return int(''.join(bin(x) for x in range(1, n+1)), 2) % 1_000_000_007
        res = ''
        for i in range(1,n+1):
            binar = format(i,"b")
            res += binar
        return int(res,2) % ((10**9)+7 )