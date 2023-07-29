# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findSecondMinimumValue(self, root: Optional[TreeNode]) -> int:
        
        self.firstMin = float('inf')
        self.secondMin= float('inf')
        
        def inOrder(root):
            if not root:
                return
            #------------------
            if root.val < self.firstMin:
                self.firstMin = root.val
            #------------------
            if root.val > self.firstMin and root.val<self.secondMin:
                self.secondMin = root.val
            #-----------------
            inOrder(root.left )
            inOrder(root.right)
            #------------------
            if root.val < self.firstMin:
                self.firstMin = root.val
            #------------------
            if root.val > self.firstMin and root.val<self.secondMin:
                self.secondMin = root.val
            #-----------------
        inOrder(root)
        # print(self.firstMin)
        # print(self.secondMin)
        return -1 if self.secondMin==float('inf') else self.secondMin