class Solution:
    def maxCompatibilitySum(self, students: List[List[int]], mentors: List[List[int]]) -> int:
        n = len(students)
        m = len(students[0])
        #basically bistmasking
        
        def isAssigned(mask,i):
            return (mask&(1<<i))>0
        
        @lru_cache(None)
        def score(i,j):
            res =0
            for x in range(m):
                if students[i][x]==mentors[j][x]:
                    res+=1
            return res
        
        @lru_cache(None)
        def compute(i,maskStudent,maskMentor):
            if i==n:
                return 0
                    
            res = 0
            for j,v in enumerate(mentors):
                if not isAssigned(maskStudent,i) and not isAssigned(maskMentor,j):
                    temp = score(i,j) +compute(i+1,maskStudent|(1<<i),maskMentor|(1<<j)) 
                    res = max(res,temp)
            return res
        res = compute(0,0,0)
        score.cache_clear()
        compute.cache_clear()
        return res