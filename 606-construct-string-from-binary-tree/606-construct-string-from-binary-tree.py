# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def tree2str(self, root: Optional[TreeNode]) -> str:
        res  =[]
        def compute(root):
            if not root : 
                return
            res.append(str(root.val))
            if not root.left and not root.right:
                return
            elif not root.left and root.right:
                res.append("()")
                res.append("(")
                compute(root.right)
                res.append(")")
                return
            elif root.left and not root.right:
                res.append("(")
                compute(root.left)
                res.append(")")
            else:
                res.append("(")
                compute(root.left)
                res.append(")")
                
                res.append("(")
                compute(root.right)
                res.append(")")
            
        compute(root)
        # print(res)
        return "".join(res)