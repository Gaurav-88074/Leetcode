class Solution:
    def validateBinaryTreeNodes(self, n: int, leftChild: List[int], rightChild: List[int]) -> bool:
        
        def compute(root,v):
            if root==-1:
                return True
            if root in v:
                return False
            v.add(root)
            left = compute( leftChild[root],v)
            right= compute(rightChild[root],v)
            
            return left and right
        v=set()
        out=[1]*n
        for i in range(n):
            a=leftChild[i]
            b=rightChild[i]
            if a!=-1:
                out[a]=0
            if b!=-1:
                out[b]=0
        if sum(out)!=1:
            return False
        start=None
        for i in range(n):
            if out[i]==1:
                start=i
                break
            
        return compute(start,v) and len(v)==n