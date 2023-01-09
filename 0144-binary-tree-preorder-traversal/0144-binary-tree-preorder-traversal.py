# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def preorderTraversal(self, root: Optional[TreeNode]) -> List[int]:
        if root==None:
            return []
        else:
            left = self.preorderTraversal(root.left)
            right =self.preorderTraversal(root.right)
            
            res = [root.val,*left,*right]
            return res