class Solution:
    def kItemsWithMaximumSum(self, a: int, b: int, c: int, k: int) -> int:
        res = 0
        if a>k:
            return k
        if a+b>=k:
            return a
        # if a+b+c
        return a-(k - (a+b))
        # if a+c < k:
        #     k-=a
        #     k+=c
        #     return -k
        # return -1
        