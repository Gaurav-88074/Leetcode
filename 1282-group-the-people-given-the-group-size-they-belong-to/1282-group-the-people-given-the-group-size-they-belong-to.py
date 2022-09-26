class Solution:
    def groupThePeople(self, groupSizes: List[int]) -> List[List[int]]:
        res = []
        d = defaultdict(list)
        value=None
        for i in range(len(groupSizes)):
            value = groupSizes[i]
            
            l = d[value]
            l.append(i)
            if len(l)==value:
                res.append(l)
                d[value]=[]
        return res