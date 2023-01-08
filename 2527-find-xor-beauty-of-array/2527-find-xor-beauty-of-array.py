class Solution:
    def xorBeauty(self, a: List[int]) -> int:
        x=0
        for i in a:x^=i
        return x