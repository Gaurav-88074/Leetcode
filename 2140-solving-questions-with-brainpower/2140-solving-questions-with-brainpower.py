class Solution:
    def mostPoints(self, questions: List[List[int]]) -> int:
        
        @lru_cache(None)
        def compute(index):
            
            if index>=len(questions):
                return 0
            
            take = questions[index][0] + compute(index + questions[index][1] + 1)
            skip = compute(index+1)
            
            return max(take,skip)
        return compute(0)