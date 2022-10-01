class LUPrefix(object):

    def __init__(self, n):
        self.arr = [0]*(n+1)
        self.res = 0
        self.p = 1
        

    def upload(self, video):
        self.arr[video]=1
        # print(self.arr)
        while self.p< len(self.arr) and self.arr[self.p]==1 :
            self.p+=1
        # self.p-=1
        

    def longest(self):
        return self.p-1
        


# Your LUPrefix object will be instantiated and called as such:
# obj = LUPrefix(n)
# obj.upload(video)
# param_2 = obj.longest()