# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def maxDepth(self, root):
        if root==None:
            return 0
        else:
            left = 1 + self.maxDepth(root.left)
            right = 1 + self.maxDepth(root.right)
            return max(left,right)

            