class Solution:
    def findDuplicate(self, paths: List[str]) -> List[List[str]]:
        d = defaultdict(list)
        
        for route in paths:
            vr = route.split(" ")
            stack = []
            if len(vr)>1:
                startRoute = vr[0]
                child = []
                for i in range(1,len(vr)):
                    file = vr[i]
                    left,right = file.split("(")
                    right = right[:-1:]
                    
                    d[right].append(startRoute +"/"+ left)
        res = []
        for array in d.values():
            if len(array)>1:
                res.append(array)
        return res
                    
                        
                    
                