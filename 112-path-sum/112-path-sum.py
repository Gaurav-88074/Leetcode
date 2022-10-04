# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def hasPathSum(self, root: Optional[TreeNode], targetSum: int) -> bool:
        def compute(root,value,pre):
            if value==targetSum and root==None and pre.left==None and pre.right==None: 
                return True
            
            if root==None: return False
            
            left = compute(root.left,value+root.val,root)
            right=compute(root.right,value+root.val,root)
            return left or right
        
        if root==None:return False
        if root.left==None and root.right==None and root.val==targetSum:
            return True
        return  compute(root,0,None);