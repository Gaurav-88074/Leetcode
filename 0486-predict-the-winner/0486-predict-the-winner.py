class Solution:
    def PredictTheWinner(self, nums: List[int]) -> bool:
        @lru_cache(None)
        def compute(i,j,size,lastTakenByFirstPersonIs):
            if size==0:
                return 0
            #----------------------------------------
            if lastTakenByFirstPersonIs==True:
                secondPersonChoice1 = compute(i+1,j,size-1 ,False)
                secondPersonChoice2 = compute(i,j-1,size-1 ,False)
                # print(f"state i={i} j={j} o_choice1 ={secondPersonChoice1}\
                # o_choice2={secondPersonChoice2}")
                return min(secondPersonChoice1,secondPersonChoice2)
            else:
                choice1 = nums[i] + compute(i+1,j,size-1 ,True)
                choice2 = nums[j] + compute(i,j-1,size-1 ,True)
                # print(f"state i={i} j={j} choice1 ={choice1}  choice2={choice2}")
                return max(choice1,choice2)
            #-------------------------------------------
            # we are taking min because we are assuming he got worst luck
            #-------------------------------------------
        n =len(nums)
        res = compute(0,n-1,n,False)
        # print(res)
        return res >= (sum(nums)-res) 
        
            