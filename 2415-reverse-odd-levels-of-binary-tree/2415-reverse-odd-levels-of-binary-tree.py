# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def reverseOddLevels(self, root):
        d = defaultdict(list)
        
        def compute(root,level):
            if root==None:
                return
            
            d[level].append(root)
            compute(root.left,level+1)
            compute(root.right,level+1)
        compute(root,0)
        for i in d:
            
            if i%2!=0:
                arr = d[i]
                values = [arr[-i].val  for i in range(1,len(arr)+1)]
                for i in range(len(arr)):
                    arr[i].val = values[i]
        return root
        