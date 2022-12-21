# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def amountOfTime(self, root: Optional[TreeNode], start: int) -> int:
        # obj = TreeNode(0)
        self.parent = defaultdict(TreeNode)
        self.snode = None
        self.res = 0
        def child(root,level):
            if root==None:
                return
            # print("at",root.val,"time =",level)
            self.res = max(self.res,level)
            child(root.left ,level + 1)
            child(root.right,level + 1)
        def find(root,key):
            #-------------------------------------
            if root==None:
                return
            #-------------------------------------
            if root.val==start:
                self.snode = root
                # return
            #-------------------------------------
            if root.left !=None:
                self.parent[root.left.val] = root
            if root.right!=None:
                self.parent[root.right.val] = root
            #-------------------------------------
            find(root.left ,key)
            find(root.right,key)
            #-------------------------------------
            
        find(root,start)
        snode = self.snode
        # print(self.snode.val)
        self.v = set()
        
        k = 1
        while snode.val!=0:
            if snode.left!=None and snode.left.val not in self.v:
                child(snode.left,k)
            if snode.right!=None and snode.right.val not in self.v:
                child(snode.right,k)
            self.v.add(snode.val)
            self.res = max(self.res,k-1)
            k+=1
            snode = self.parent[snode.val]
        return self.res