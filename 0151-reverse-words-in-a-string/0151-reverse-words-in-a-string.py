class Solution:
#     def reverse(self,c,low,high){
#         # char p;
#         while low<high:
#             p = c[low]
#             c[low] = c[high]
#             c[high] = p
            
#             low+=1
#             high-=1
        
    
    def reverseWords(self, s: str) -> str:
        arr = s.strip().split(" ")
        arr = arr[::-1]
        for i in range(len(arr)):
            arr[i] = arr[i].strip()
            
        res = []
        for i in arr:
            if i!='':
                res.append(i)
        return " ".join(res)