# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def widthOfBinaryTree(self, root: Optional[TreeNode]) -> int:
        d = defaultdict(list)
        self.res = 0
        def compute(root,level,value):
            if not root:
                return 
            #----------------------------------
            d[level].append(value)
            self.res = max(self.res,d[level][-1] - d[level][0] + 1 )
            #------------------------------------
            compute(root.left ,level + 1,(2 * value))
            compute(root.right,level + 1,(2 * value) + 1)
            
        compute(root,1,1)
        # print(d)
        return self.res