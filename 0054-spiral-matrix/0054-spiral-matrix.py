class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        res=[]
        
        ele = len(matrix) * len(matrix[0])
        
        left = 0
        right= len(matrix[0])-1
        
        top = 0
        down= len(matrix)-1
        
        while top<=down and left<=right:
            # print(left,right,top,down)
            if top==left and right==down and top==down:
                res.append(matrix[left][left])
                break
            
            #Going from left to right
            if left<=right:
                for i in range(left,right):
                    res.append(matrix[top][i])
                
            #Going from top to down
            if top<=down:
                for i in range(top,down+1):
                    res.append(matrix[i][right])
                
            #Going from right to left
            if left<=right and top!=down:
                for i in range(right-1,left-1,-1):
                    res.append(matrix[down][i])
                
            #Going from down to top
            if top<=down and left!=right:
                for i in range(down-1,top,-1):
                    res.append(matrix[i][left])
            
            #------------------
            #changing layers
            top  +=1
            left +=1
            right-=1
            down -=1

        # while len(res)!=ele : res.pop()
        return res
        