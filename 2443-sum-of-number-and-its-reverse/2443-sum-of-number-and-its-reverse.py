class Solution:
    def sumOfNumberAndReverse(self, num: int) -> bool:
        v = num
        for i in range(num+1):
            a = i
            b = int(str(i)[::-1])
            if a+b==v:return True
        return False