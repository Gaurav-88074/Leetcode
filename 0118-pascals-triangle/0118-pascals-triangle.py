class Solution:
    def generate(self, n: int) -> List[List[int]]:
        res = [[1]]
        
        for i in range(n-1):
            arr = []
            preArr  =res[-1]
            x  =len(preArr)
            arr.append(1)
            for j in range(1,x):
                arr.append(preArr[j]+preArr[j-1])
            arr.append(1)
            res.append(arr)
        return res