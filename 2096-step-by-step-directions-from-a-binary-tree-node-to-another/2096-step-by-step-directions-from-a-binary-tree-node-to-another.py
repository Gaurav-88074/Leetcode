# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def getDirections(self,root,sv,dv):
        self.lca = None 
        self.r   = [] 

        self.startFound = False
        self.destFound = False
        self.startLevel = None 
        self.lcaLevel = None
        def getLCA(root,level):
            if not root:  
                return 0
            #------------------------------
            left = getLCA(root.left ,level+1)
            right= getLCA(root.right,level+1)
            #------------------------------
            res = left + right 
            #-------------------------------
            if root.val==sv:
                res+=1  
                self.startFound = True 
                self.startLevel = level
            if root.val==dv:
                res+=1
                # self.destFound  = True 
            #--------------------------------
            if res==2 and self.lca==None:
                self.lca = root  
                self.lcaLevel = level
            #---------------------------
            return res 
            #--------------------------
        #-------------------------
        getLCA(root,0)
        #-------------------------
        def destRoute(root,d): 
            if not root or self.destFound==True: 
                return   
            #----------------------------
            destRoute(root.left,-1)
            destRoute(root.right,1)
            #----------------------------
            if root.val==dv:
                self.destFound  = True 
            #----------------------------
            if self.destFound==True and root!=self.lca: 
                if d==-1:  
                    self.r.append("L")
                elif d==1 : 
                    self.r.append("R")
            #-------------------------------------------
        destRoute(self.lca,0)
        # print(self.lca.val)
        rs = list(reversed(self.r))
        # print(rs)
        h = abs(self.startLevel - self.lcaLevel)
        # print(h)
        res = h*"U"+"".join(rs)
        return res