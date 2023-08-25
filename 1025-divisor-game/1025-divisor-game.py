class Solution:
    def divisorGame(self, n: int) -> bool:
        #P_id
        #1 -> Alice
        #0 -> BOB
        
#         def compute(n,p):
            
#             if n==1:
#                 return p==0
            
#             res = False
#             for x in range(1,n):
#                 if n%x==0:
#                     res = res or  compute(n-x,1-p)
#             return res
#         return compute(n,1)
        
        return (n&1)==0