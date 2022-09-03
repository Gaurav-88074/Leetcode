class Solution:
    def numsSameConsecDiff(self, n: int, k: int) -> List[int]:
        self.value = 0
        self.res = []
        def compute(n,k):
            if n==0:
                # print(self.value)
                self.res.append(self.value)
                return
            else:
                for i in range(0,10):
                    if abs(self.value%10-i)==k:
                        self.value = self.value*10+i
                        compute(n-1,k)
                        self.value = (self.value)//10
        for i in range(1,10):
            self.value = i;
            compute(n-1,k)
            # self.value = 0
        return self.res
                        