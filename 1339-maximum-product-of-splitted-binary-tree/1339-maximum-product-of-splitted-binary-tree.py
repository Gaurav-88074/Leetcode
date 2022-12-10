# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxProduct(self, root: Optional[TreeNode]) -> int:
        def computeSum(root):
            if not root : return 0
            left = computeSum(root.left)
            right= computeSum(root.right)
            return root.val + left + right
        res = [0]
        mod = 10**9+7
        total = computeSum(root)
        def compute(root,res):
            if not root:
                return 0
            left = compute(root.left,res)
            right= compute(root.right,res)
            res[0]  = max(res[0],(total-left ) * left)
            res[0]  = max(res[0],(total-right) * right)
            # res[0] %= mod
            return root.val+left+right
        compute(root,res)
        return res[0]%mod