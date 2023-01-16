# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def smallestFromLeaf(self, root: Optional[TreeNode]) -> str:
        arr = []
        res = []
        def compute(root):
            if not root:
                # print(arr)
                return
            if root.left==None and root.right==None:
                arr.append(chr(root.val+97))
                # print(arr)
                res.append("".join(arr[::-1]))
                
                arr.pop()
                return
            arr.append(chr(root.val+97))
            compute(root.left)
            compute(root.right)
            arr.pop()

        compute(root)
        # print(res)
        res.sort()
        return res[0]