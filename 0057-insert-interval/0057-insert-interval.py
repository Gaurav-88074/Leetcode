class Solution:
    def insert(self, intervals, x):
        res =  intervals
        res.append(x)
        
        res.sort(key = lambda v : v[0])
        
        stack = [res[0]]
        
        for i in range(1,len(intervals)):
            if intervals[i][0]<= stack[-1][1]:
                stack[-1][1] = max(stack[-1][1],intervals[i][1])
            else:
                stack.append(intervals[i])
        return stack