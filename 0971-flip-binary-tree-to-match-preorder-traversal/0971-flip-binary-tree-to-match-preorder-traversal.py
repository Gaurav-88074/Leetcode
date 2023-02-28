# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def flipMatchVoyage(self, root: Optional[TreeNode], voyage: List[int]) -> List[int]:
        self.i = 0
        v = voyage
        res = []
        
        def compute(root):
            if not root:
                return True
            if root.val!=v[self.i]:
                return False
            self.i+=1
            if root.left!=None and root.left.val!=v[self.i]:
                res.append(root.val)
                return compute(root.right) and compute(root.left) 
            return compute(root.left) and compute(root.right)
        ans= compute(root)
        if not ans : return [-1]
        return res
            
            
            