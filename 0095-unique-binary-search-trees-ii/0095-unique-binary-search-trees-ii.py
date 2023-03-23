# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def generateTrees(self, n: int) -> List[Optional[TreeNode]]:
        
        def preorder(root,res):
            if not root:
                return
            res.append(root.val)
            preorder(root.left ,res)
            preorder(root.right,res)
        @lru_cache(None)
        def compute(left,right):
            if left>right:
                return []
            if left==right:
                return [TreeNode(left)]
            res = []
            for i in range(left,right+1):
                leftNodes = compute(left , i-1)
                rightNodes= compute(i+1  ,right)
                #---------------------------------
                if len(leftNodes)==0:
                    for b in rightNodes:
                        root = TreeNode(i,None,b)
                        res.append(root)
                #--------------------------------
                if len(rightNodes)==0:
                    for a in leftNodes:
                        root = TreeNode(i,a,None)
                        res.append(root)
                #--------------------------------
                for a in leftNodes:
                    for b in rightNodes:
                        root = TreeNode(i,a,b)
                        res.append(root)
                #--------------------------------
                
            # print(res)
            return res
        
        ans=compute(1,n)
        # print(ans)
        return ans