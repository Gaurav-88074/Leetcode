class Solution:
    def numTrees(self, n: int) -> int:
        #------------------------------
        @lru_cache(None)
        def compute(left,right):
            if left>right:
                return 0
            if left==right:
                return 1
            res = 0
            for i in range(left,right+1):
                leftNodes = compute(left , i-1)
                rightNodes= compute(i+1  ,right)
                #---------------------------------
                if leftNodes==0:
                    res+= rightNodes
                #--------------------------------
                elif rightNodes==0:
                    res+= leftNodes
                #--------------------------------
                else:
                    res+= leftNodes*rightNodes
                #--------------------------------
            return res
        return compute(1,n)
        
            