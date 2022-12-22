# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def subtreeWithAllDeepest(self, root: TreeNode) -> TreeNode:
        d = defaultdict(list)
        self.mx = 0
        self.res =-1
        def go(root,level):
            if root==None:
                return
            d[level].append(root.val)
            self.mx = max(self.mx,level)
            go(root.left ,level+1)
            go(root.right,level+1)
        go(root,0)
        # print(d[self.mx])
        self.arr = set(d[self.mx])
        def compute(root):
            if not root:
                return 0
            left = compute(root.left)
            right= compute(root.right)
            # if root.val in self.arr:
            #     return 1
            # r=[*left,*right]
            r=left+right
            if root.val in self.arr: 
                r+=1
            if self.res==-1 and r==len(self.arr):
                self.res = root
            # print("lca at node",root.val," is ",r)
            return r
        compute(root)
        return self.res