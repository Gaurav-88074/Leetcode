class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        m = len(matrix)
        n = len(matrix[0])
        
        def giveMatrixCoordinate(i):
            # 0 = 0,0
            # 3 = 0,3
            # 6 = 1,2
            x = i//n
            y = i%n
            return [x,y]
        # print(0,giveMatrixCoordinate(0))
        # print(3,giveMatrixCoordinate(3))
        # print(6,giveMatrixCoordinate(6))
        # print(10,giveMatrixCoordinate(10))
        low = 0
        high= (m*n)-1
        while low<=high:
            mid = (low+high)//2
            x,y = giveMatrixCoordinate(mid)
            if matrix[x][y]==target:
                return True
            elif target < matrix[x][y]:
                high = mid-1
            else:
                low = mid+1
        return False