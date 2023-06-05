class Solution:
    def checkStraightLine(self, coordinates: List[List[int]]) -> bool:
        a = coordinates[0]
        b = coordinates[1]
        def computeSlope(node):
            return (b[1]-a[1])*(node[0]-b[0]) == (node[1]-b[1])*(b[0]-a[0])
        #use brain
        for i in range(1,len(coordinates)):
            if not computeSlope(coordinates[i]):
                return False
        return True