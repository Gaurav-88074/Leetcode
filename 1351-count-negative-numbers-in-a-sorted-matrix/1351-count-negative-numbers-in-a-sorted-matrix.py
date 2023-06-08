class Solution(object):
    def countNegatives(self, grid):
        res = 0
        for i in grid:
            for j in i:
                if j<0:
                    res+=1
        return res
        