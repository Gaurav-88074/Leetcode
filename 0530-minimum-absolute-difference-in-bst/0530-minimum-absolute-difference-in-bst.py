# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def inOrder(self,root,l):
        if root==None:
            return
        self.inOrder(root.left,l)
        l.append(root.val)
        self.inOrder(root.right,l)
        
    def getMinimumDifference(self, root):
        l=[]
        self.inOrder(root,l)
        m = float('inf')
        for i in range(1,len(l)):
            m = min(m,l[i]-l[i-1])
        return m
        