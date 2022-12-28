# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class CBTInserter:

    def __init__(self, root: Optional[TreeNode]):
        self.h = 0;
        self.pos = 0;
        self.d = defaultdict(int)
        self.root=root
        def dfs(root,level):
            if root==None:
                return
            dfs(root.left ,level + 1)
            dfs(root.right,level + 1)
            self.h = max(self.h,level)
            self.d[level]+=1
        dfs(root,0)
        # print(self.d,self.h,self.pos)
        maxNodes = 1<<self.h 
        # self.d[self.h]+=1 
        if self.d[self.h]==maxNodes: 
            self.h+=1 
            # self.pos=1 
            self.d[self.h]=1
        else:
            # self.pos = self.d[self.h] + 1 
            self.d[self.h]+=1
        # print(self.h,self.pos)

    def insert(self, val: int) -> int:  
        hashmap = defaultdict(int)
        self.now = None
        def perform(root,level,hashmap):
            hashmap[level]+=1
            if root==None: 
                if level==self.h and self.d[self.h]==hashmap[level]:
                    return [TreeNode(val),True]
                return [None,False]
            root.left ,check = perform(root.left ,level+1,hashmap)
            if check:self.now = root
            root.right,check = perform(root.right,level+1,hashmap)
            if check:self.now = root
            return [root,False] 
        self.root ,check= perform(self.root,0,hashmap)
        if check:self.now = root
        #-----------------------------  
        # hashmap[self.h]+=1
        maxNodes = 1<<self.h  
        # print(self.d)
        if self.d[self.h]==maxNodes: 
            # print("while adding",val)
            self.h+=1 
            self.d[self.h]=1
        else:
            self.d[self.h]+=1
        #-----------------------------
        return self.now.val

    def get_root(self) -> Optional[TreeNode]:
        return self.root


# Your CBTInserter object will be instantiated and called as such:
# obj = CBTInserter(root)
# param_1 = obj.insert(val)
# param_2 = obj.get_root()