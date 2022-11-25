class Solution:
    def rankTeams(self, votes: List[str]) -> str:
        size = len(votes[0])
        
        d = [[0]*128 for i in range(size)]
        
        for vote in votes:
            for i in range(size):
                char = ord(vote[i])
                d[i][char]+=1
            
        #-----------------------
        arr = list(votes[0])
        #-------------------------------------
        def comp(a,b):
            for i in range(size):
                if d[i][a] != d[i][b]:
                    return d[i][b]-d[i][a]
            return a-b
        
        arr = list(map(ord,arr))
        arr.sort(key = cmp_to_key(comp))
        # arr.reverse()
        arr = list(map(chr,arr))
        # print("verdict",arr)
        #-------------------------------------
        return "".join(arr)