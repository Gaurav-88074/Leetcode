# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findTilt(self, root: Optional[TreeNode]) -> int:
        self.res= 0
        def compute(root):
            if not root:
                return 0
            left = compute(root.left)
            right= compute(root.right)
            pre = root.val
            root.val = abs(left-right)
            self.res+=root.val
            return left + right+pre
        compute(root)
        return self.res