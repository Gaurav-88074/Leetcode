class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        pre = 0
        m = defaultdict(int)
        res = 0
        for i,v in enumerate(fruits):
            m[v]+=1
            while len(m)>2:
                m[fruits[pre]]-=1
                if m[fruits[pre]]==0:
                    del m[fruits[pre]]
                pre+=1
            # print(m,pre,i,i - pre + 1)
            res = max(res, i - pre + 1)
        return res 