# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isCousins(self, root: Optional[TreeNode], x: int, y: int) -> bool:
        d=defaultdict(set)
        pr = dict()
        def dfs(root,i,p):
            if not root:
                return
            d[i].add(root.val)
            pr[root.val]=p
            dfs(root.left,i+1,root.val)
            dfs(root.right,i+1,root.val)
        dfs(root,1,-1)
        if pr[x]==pr[y]:return False
        for i in d:
            if x in d[i] and y in d[i]:
                return True
        return False
        
        