class Solution:
    def ways(self, pizza: List[str], k: int) -> int:
        # ['A', '.', '.'][00,01,02]
        # ['A', 'A', 'A'][10,11,12]
        # ['.', '.', '.'][20,21,22]
        rows = len(pizza)-1
        cols = len(pizza[0])-1
        mod = 10**9 + 7
    
        def displayGrid(start_row,start_col,end_row,end_col):
            s = ""
            for i in range(start_row,end_row+1):
                for j in range(start_col,end_col+1):
                    s+=pizza[i][j]+" "
                if i!=end_row:
                    s+="\n"
            print("****",start_row,start_col,end_row,end_col)
            print(s)
            print("****")
        #--------------------------------------
        @lru_cache(None)
        def hasApple(start_row,start_col,end_row,end_col):
            for i in range(start_row,end_row+1):
                for j in range(start_col,end_col+1):
                    if pizza[i][j]=="A":
                        return True
            return False
        #--------------------------------------
        @lru_cache(None)
        def compute(curr_row,curr_col,cut):
            if cut==0:
                # displayGrid(start_row,start_col,end_row,end_col)
                return 1 if hasApple(curr_row,curr_col,rows,cols)==True else 0
            
            res = 0
            
            #-----------------
            #Traversing with knife vertically [top - bottom].
            #I'm literlly using my brain too much
            #-----------------
            for i in range(curr_row+1,rows+1):
                isFeasible = hasApple(curr_row,curr_col,i-1,cols)
                if isFeasible:
                    res += compute(i,curr_col,cut-1)%mod
            #-----------------
            #-----------------
            #Traversing with knife horizontally [left- right].
            #-----------------
            for i in range(curr_col+1,cols+1):
                isFeasible = hasApple(curr_row ,curr_col,rows,i-1)
                if isFeasible:
                    res+=compute(curr_row ,i ,cut-1)%mod
            #-----------------
            return res
        if k==1 :  return 1 if hasApple(0,0,rows,cols) else 0
        res= compute(0,0,k-1)%mod
        hasApple.cache_clear()
        compute.cache_clear()
        return res
            