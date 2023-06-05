class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        a = coordinates[0]
        b = coordinates[1]
        def computeSlope(node):
            return (b[1]-a[1])*(node[0]-b[0]) == (node[1]-b[1])*(b[0]-a[0])
        # slope = computeSlope(a,b)
        # print(slope)
        for i in range(1,len(coordinates)):
            # node = coordinates[i]
            v=computeSlope(coordinates[i])
            if v==False:
                return v
            # if slope!=v:
                # return False
        return True