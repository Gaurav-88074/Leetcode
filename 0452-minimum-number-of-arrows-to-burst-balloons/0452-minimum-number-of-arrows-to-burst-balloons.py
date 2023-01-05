class Solution(object):
    def findMinArrowShots(self, points):
        points.sort(key = lambda x : x[1] )
        res = 1
        pre = points[0]
        for i in range(1,len(points)):
            if points[i][0]> pre[1]:
                res+=1
                pre = points[i]
        return res
        