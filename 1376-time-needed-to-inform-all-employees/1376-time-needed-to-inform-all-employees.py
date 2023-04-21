class Solution:
    def numOfMinutes(self, n: int, headID: int, manager: List[int], informTime: List[int]) -> int:
        d = defaultdict(list)
        for i,v in enumerate(manager):
            if v!=-1:
                d[v].append(i)
        # print(d)
        self.res = 0
        def compute(node,v):
            if len(d[node])==0:
                self.res = max(self.res,v)
                return 0
            time = informTime[node]
            for i in d[node]:
                compute(i,v + time)
        compute(headID,0)
        return self.res