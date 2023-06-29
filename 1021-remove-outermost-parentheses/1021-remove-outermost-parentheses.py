class Solution:
    def removeOuterParentheses(self, s: str) -> str:
        res = []
        b = 0
        d = defaultdict(int)
        preScene = 0
        for i,v in enumerate(s):
            if v=="(":
                b+=1
            else:
                b-=1
            if b==0:
                start = preScene + 1
                end  = i
                # print(start,end)
                res.append(s[ start : end ])
                preScene = i+1
        # print(res)
        return "".join(res)
            
                
#         temp = []
#         res = []
#         for index,i in enumerate(s):
#             if res and res[-1]=="(":
#                 if i==")":
#                     res.append(i)
#                 else:
#                     res.pop()
#                     res.append(i)
#             elif res and res[-1]==")":
#                 if i==")":
#                     continue
#                 else:
#                     res.append(i)
                
#             else:
#                 res.append(i)
#             print(index,"->",res)
#         print(res)
#         return "".join(res)