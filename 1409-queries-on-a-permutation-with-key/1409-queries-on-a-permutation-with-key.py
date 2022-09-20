class Solution:
    def processQueries(self, queries: List[int], m: int) -> List[int]:
        arr = [i for i in range(1,m+1)]
        
        res = []
        for q in queries:
            index = arr.index(q)
            res.append(index)
            
            arr.remove(q)
            arr.insert(0,q)
        return res