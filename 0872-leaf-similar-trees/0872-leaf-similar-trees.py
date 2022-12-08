# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def leafSimilar(self, root1, root2):
        a=[]
        b=[]
        def dfs(root,l):
            if root==None:return
            
            if root.left==None and root.right==None:
                l.append(root.val)
            dfs(root.left,l)
            dfs(root.right,l)
        dfs(root1,a)
        dfs(root2,b)
        return a==b