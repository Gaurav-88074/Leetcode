class Solution:
    def numberOfWeakCharacters(self, properties: List[List[int]]) -> int:
        def comp(a,b):
            if a[0]==b[0] : return b[1]-a[1]
            return a[0]-b[0]
        properties.sort(key = cmp_to_key(comp))
        
        res = 0
        # print(properties)
        #------------------------------------------
        arr = [0]*len(properties)
        
        stack = [-1]
        for i in range(len(properties)-1,-1,-1):
            while stack[-1]!=-1 and stack[-1]<=properties[i][1]:
                stack.pop()
            arr[i] = stack[-1]
    
            stack.append(properties[i][1])
        #----------------------------------------------
        # print(arr)
        for i in range(len(properties)):
            if arr[i]!=-1 :
                res+=1
        return res