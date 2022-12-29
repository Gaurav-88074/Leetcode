class Solution:

    def __init__(self, n: int, blacklist: List[int]):
        self.p1 = 0
        self.p2 = 1
        self.arr =  blacklist
        self.arr.append(n)
        self.arr.append(-1)
        self.arr.sort()
        self.n = n
        # print(self.arr[-1])
        self.vrr = []
        for i in range(0,len(self.arr)-1):
            if abs(self.arr[i+1]-self.arr[i])==1: 
                continue 
            else:
                self.vrr.append(
                    [
                        self.arr[i]+1,self.arr[i+1]
                    ]
                )
        # print(self.vrr)
        self.i = 0
        self.size = len(self.vrr)

    def pick(self) -> int:
        # return -1
        if len(self.arr)<=2: return random.randrange(0,self.n)
        # while abs(self.arr[self.p2]-self.arr[self.p1])==1 or self.p2==0:
        #     self.p1+=1
        #     self.p2+=1
        #     self.p1%=self.size
        #     self.p2%=self.size
        ## print(self.arr[self.p1]+1,self.arr[self.p2])
        # res =  random.randrange(self.arr[self.p1]+1,self.arr[self.p2])
        # self.p1+=1
        # self.p2+=1
        # self.p1%=self.size
        # self.p2%=self.size
        a,b = self.vrr[self.i]
        self.i+=1
        self.i%=self.size
        return random.randrange(a,b)
            
