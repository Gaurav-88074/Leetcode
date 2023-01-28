from sortedcontainers import SortedList, SortedDict,SortedSet
class SummaryRanges:

    def __init__(self):
        self.l = SortedList(key = lambda x : x[0] )
        # self.l = SortedSet()
        self.st = set()
    def addNum(self, val: int) -> None:
        if val in self.st:
            return
        self.st.add(val)
        
        self.l.add([val,val])

    def getIntervals(self) -> List[List[int]]:
        res = []
        for i in self.l:
            # print(self.l)
            if len(res)>0 and abs(res[-1][1] - i[0])==1:
                # print(res,i,(res[-1][1] - i[0]))
                res[-1][1] = i[0]
            else:
                res.append([*i])

        return res


# Your SummaryRanges object will be instantiated and called as such:
# obj = SummaryRanges()
# obj.addNum(val)
# param_2 = obj.getIntervals()