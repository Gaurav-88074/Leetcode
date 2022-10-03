class Solution:
    def findingUsersActiveMinutes(self, logs: List[List[int]], k: int) -> List[int]:
        res = [0] * k
        
        d = defaultdict(set)
        
        for _id,time in logs:
            d[_id].add(time)
            
        for value in d.values():
            v = len(value)
            res[v-1]+=1
        return res