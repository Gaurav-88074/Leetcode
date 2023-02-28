# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def findDuplicateSubtrees(self, root: Optional[TreeNode]) -> List[Optional[TreeNode]]:
        d = defaultdict(str)
        c = defaultdict(int)
        def compute(root,route):
            if not root:
                return ""
            left = compute(root.left,"L")
            right= compute(root.right,"R")
            #-------------------------------
            res = left +"-"+ str(root.val)+"-"+ right
            #-----------------------------------------
            d[res] = root
            c[res]+=1
            return route+res
        compute(root,"")
        # print(c)
        ans =[]
        for i in c:
            if c[i]>1:
                ans.append(d[i])
                
        return ans