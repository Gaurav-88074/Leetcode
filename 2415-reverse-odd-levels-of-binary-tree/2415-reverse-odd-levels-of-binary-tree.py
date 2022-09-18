# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        d = defaultdict(list)
        
        def compute(root,level):
            if root==None:
                return
            
            d[level].append(root.val)
            compute(root.left,level+1)
            compute(root.right,level+1)
        compute(root,0)
        # print(d)
        # for i in d:
        #     if (i&1)==1:
        #         d[i] = list(reversed(d[i]))
        # print(d)
        def visit(root,level):
            if root==None:
                return
            
            if (level%2)==1:
                root.val = d[level].pop()
            visit(root.left,level+1)
            visit(root.right,level+1)
        # print(d)
        visit(root,0)
        return root
                