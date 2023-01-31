class Solution:
    def bestTeamScore(self, scores: List[int], ages: List[int]) -> int:
        arr = []
        for i in range(len(scores)):
            arr.append(
                [ scores[i] , ages[i] ]
            )
        arr.sort(key = lambda x : (x[1],x[0]))
        
        @lru_cache(None)
        def compute(index,prevIndex):
            if index==len(arr):
                return 0
            
            take = 0
            skip = 0
            
            if prevIndex==-1:
                take = arr[index][0] + compute(index+1,index)
            # elif arr[index][1] == arr[prevIndex][1]:
            #     take = arr[index][0] + compute(index+1,index)
            elif arr[index][0] >= arr[prevIndex][0]:#and arr[index][0] >=arr[prevIndex][0]:
                take = arr[index][0] + compute(index+1,index)
                
#             elif arr[index][1] < arr[prevIndex][1] and arr[index][0] <= arr[prevIndex][0]:
#                 take = arr[index][0] + compute(index+1,index)
                
            skip = compute(index+1,prevIndex)
            return max(take,skip)
        
        return compute(0,-1)