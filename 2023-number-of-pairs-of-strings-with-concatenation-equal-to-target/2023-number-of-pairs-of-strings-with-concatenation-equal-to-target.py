class Solution:
    def numOfPairs(self, nums: List[str], target: str) -> int:
        d = defaultdict(int)
        res = 0
        
        for i in nums:
            d[i]+=1
        for v in nums:
            till = len(v)
            if till>=len(target):
                continue
            else:
                left = target[ : till]
                if left == v:
                    right= target[till: ]
                    
                    res+=d[right]
                    if left==right:
                        res-=1
        return res
        