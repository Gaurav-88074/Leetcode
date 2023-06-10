# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: Optional[TreeNode]) -> bool:
        if not root : return True
        val = root.val
        def compute(root):
            if not root:
                return True
            return root.val==val and compute(root.left) and compute(root.right)
        return compute(root)
        