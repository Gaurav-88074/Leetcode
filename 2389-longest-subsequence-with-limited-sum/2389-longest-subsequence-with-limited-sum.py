class Solution:
    def answerQueries(self, nums: List[int], queries: List[int]) -> List[int]:
        nums.sort()
        res = []
        for size in queries:
            s=0
            i=0
            v =0
            while i<len(nums) and s<=size:
                s+=nums[i]
                if(s<=size):
                    v+=1
                else:
                    break
                i+=1
                
            # print(s)
            res.append(v)
        return res