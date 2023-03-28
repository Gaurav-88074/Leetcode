class Solution:
    def mincostTickets(self, days: List[int], costs: List[int]) -> int:
        
        @lru_cache(None)
        def compute(i,passDeadline):
            
            if i==len(days):
                return 0
            if passDeadline < days[i]:
                return  min([
                    costs[0] + compute(i+1, 0 +  days[i]),
                    costs[1] + compute(i+1, 6 +  days[i]),
                    costs[2] + compute(i+1, 29+  days[i])
                ])
            return compute(i+1 , passDeadline)
        return compute(0,-1)
            