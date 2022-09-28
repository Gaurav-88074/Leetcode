class UndergroundSystem:

    def __init__(self):
        self.d =dict()
        self.score=defaultdict(int)
        self.count=defaultdict(int)

    def checkIn(self, id: int, stationName: str, t: int) -> None:
        self.d[id] = [stationName,t]

    def checkOut(self, id: int, stationName: str, t: int) -> None:
        enterStation,enterTime = self.d[id]
        key = (enterStation , stationName)
        self.score[key]+=(t-enterTime)
        self.count[key]+=1
        

    def getAverageTime(self, startStation: str, endStation: str) -> float:
        key = (startStation, endStation)
        # print(self.score)
        return self.score[key]/self.count[key]


# Your UndergroundSystem object will be instantiated and called as such:
# obj = UndergroundSystem()
# obj.checkIn(id,stationName,t)
# obj.checkOut(id,stationName,t)
# param_3 = obj.getAverageTime(startStation,endStation)