class Solution:
    def countGood(self, nums: List[int], k: int) -> int:
        pair = 0
        d = defaultdict(int)
        res = 0
        pre = 0
        for i,v in enumerate(nums):
            d[v]+=1
            if d[v]>=2:
                n =d[v]
                pair+= n-1
            # print(pair,"[",i,",",v,"]")

            while pair>=k and pre<i:
                # res+=1
                key = nums[pre]
                value = d[key]
                if value>=2:
                    pair -= (value-1)
                value-=1
                if value==0:
                    del d[key]
                else:
                    d[key]-=1
                #---------
                pre+=1
                #----------
            res+=pre
        return res