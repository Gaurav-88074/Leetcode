# Definition for a binary tree node.
# class TreeNode(object):
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution(object):
    def isPresent(self,root,target):
        if root==None:
            return False
        elif target == root.val:
            return True
        elif target<root.val:
            return self.isPresent(root.left,target)
        else:
            return self.isPresent(root.right,target)
    def inOrder(self,root,l):
        if root==None:
            return
        self.inOrder(root.left,l)
        l.append(root.val)
        self.inOrder(root.right,l)
    def findTarget(self, root, k):
        l = []
        self.inOrder(root,l)
        low = 0
        high = len(l)-1
        while low<high:
            if l[low]+l[high] == k:
                return True
            elif l[low]+l[high] < k:
                low+=1
            elif l[low]+l[high] > k:
                high-=1
        return False
        