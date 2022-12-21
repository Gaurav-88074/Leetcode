# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxSumBST(self, root: Optional[TreeNode]) -> int:
        self.res = float('-inf')
        def compute(root):
            if root==None:
                return [0,True,0,0]
            left ,isLeftBST ,l_min,l_max = compute(root.left)
            right,isRightBST,r_min,r_max = compute(root.right)
            # print("at",root.val,left,right)
            
            if root.left!=None and root.right!=None:
                # print("comparing 1 at ",root.val)
                st1 = isLeftBST and isRightBST
                st2 = root.val<r_min  and root.val>l_max
                if root.left.val < root.val and root.right.val>root.val and st1 and st2:
                    value = left + right + root.val
                    self.res = max(self.res,value)
                    
                    return [value,True,min(l_min,root.val,r_min),max(l_max,root.val,r_max)]
                else:
                    return [0,False,float('inf'),float('-inf')]
            elif root.left==None and root.right!=None:
                if root.val<root.right.val and isRightBST and r_min > root.val:
                    value = right + root.val
                    self.res = max(self.res,value)
                     
                    return [value ,True,min(root.val,r_min),max(root.val,r_max)]
                else:
                    return [0,False,float('inf'),float('-inf')]
            elif root.left!=None and root.right==None:
                if root.left.val < root.val and isLeftBST and l_max < root.val:
                    value = left + root.val
                    self.res = max(self.res,value)
                     
                    return [value , True,min(root.val,l_min),max(root.val,l_max)]
                else:
                    return [0,False,float('inf'),float('-inf')]
            else:
                self.res = max(self.res,root.val)
                return [root.val,True,root.val,root.val]
        v,isBST,r_min,r_max = compute(root)
        # print(v)
        if isBST:
            self.res = max(self.res,v)
        return self.res if self.res>0 else 0