# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def allPossibleFBT(self, x: int) -> List[Optional[TreeNode]]:
        
        @lru_cache(None)
        def compute(n):
            if n<=0:
                return []
            
            if n==1:
                return [TreeNode(0)]
            
            res = []
            #----------
            # n-=1
            #---------
            #-----------------------------
            # if (n)%2==0:
            # left = compute(n//2)
            # right= compute(n//2)
            # for a in left :
            #     for b in right:
            #         root = TreeNode(0,a,b)
            #         res.append(root)
            #--------------------------------
#             left = compute(1)
#             right= compute(n-1)
#             for a in left :
#                 for b in right:
                    
#                     root = TreeNode(0,a,b)
#                     res.append(root)
#             #----------------------------------   
#             left = compute(n-1)
#             right= compute(1)
#             for a in left :
#                 for b in right:
#                     root = TreeNode(0,a,b)
#                     res.append(root)
            #-----------------------------------
            for i in range(2, n + 1, 2):
                left = compute(i-1)
                right= compute(n-i)
                for a in left :
                    for b in right:
                        root = TreeNode(0,a,b)
                        res.append(root)
            return res
                #------------------------------------
        res = compute(x)
        return res