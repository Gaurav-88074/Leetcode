class Solution:
    def pivotInteger(self, n: int) -> int:
        v = 0
        left = []
        for i in range(1,n+1):
            v+=i
            left.append(v)
        v = 0
        right = []
        for i in range(n,0,-1):
            v+=i
            right.append(v)
        right.reverse()
        
        a = 0
        b = n-1
        # print(left)
        # print(right)
        for i in range(n):
            if left[i]==right[i]:
                return i+1
        return -1
        