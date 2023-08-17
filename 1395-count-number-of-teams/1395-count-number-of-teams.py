class Solution:
    def numTeams(self, rating: List[int]) -> int:
        #----------------------------------
        n  =len(rating)
        noeGreaterThan = [0] * n
        noeLesserThan  = [0] * n
        for i in range(n):
            for j in range(i+1,n):
                #-----------------------
                if rating[i]<rating[j]:
                    noeGreaterThan[i]+=1
                #-----------------------
                if rating[i]>rating[j]:
                    noeLesserThan[i] +=1
                #-----------------------
                    
        @lru_cache(None)
        def computeINC(i,pre):
            if i==len(rating):
                return 0
            take = 0
            skip = 0
            if pre==None:
                take = computeINC(i+1,i)
            else:
                if rating[pre]<rating[i]:
                    take += noeGreaterThan[i]
                if rating[pre] > rating[i]:
                    take += noeLesserThan[i]
            skip = computeINC(i+1,pre)
            
            return take+skip
        #----------------------------------
        @lru_cache(None)
        def computeDEC(i,pre):
            if i==len(rating):
                return 0
            take = 0
            skip = 0
            if pre==None:
                take = computeDEC(i+1,i)
            else:
                if rating[pre] > rating[i]:
                    take = noeLesserThan[i]
            skip = computeDEC(i+1,pre)
            
            return take+skip
        #-------------------------------------
        res1 = computeINC(0,None)
        computeINC.cache_clear()
        # res2 = computeDEC(0,None)
        # computeDEC.cache_clear()
        #---------------------------------
        return res1 #+ res2