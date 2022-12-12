class Allocator:

    def __init__(self, n: int):
        self.arr = [None]*n
        self.p = 0
        self.n = n
        self.space = n

    def allocate(self, size: int, mID: int) -> int:
        if size>self.space:
            return -1
        ch=False
        arr = self.arr
        c = 0
        mx = 0
        
        p=None
        for i in range(self.n):
            if arr[i]==None:
                c+=1
                mx = max(mx,c)
                if mx>=size:
                    # print("hn hua",i+1-mx)
                    p = i+1-mx
                    break
            else:
                mx = max(mx,c)
                if mx>=size:
                    # print("hn hua",i+1-mx)
                    p = i+1-mx
                    break
                c  = 0
        mx = max(mx,c)
        if mx>=size:
            # print("hn hua",i+1-mx)
            p = i+1-mx
        if p!=None:
            for i in range(p,p+size):
                self.arr[i] = mID
            return p
        # print("allocate",mx,p)
        return -1
                
    def free(self, mID: int) -> int:
        c = 0
        for i in range(self.n):
            if self.arr[i]==mID:
                self.arr[i]=None
                c+=1
        return c


# Your Allocator object will be instantiated and called as such:
# obj = Allocator(n)
# param_1 = obj.allocate(size,mID)
# param_2 = obj.free(mID)