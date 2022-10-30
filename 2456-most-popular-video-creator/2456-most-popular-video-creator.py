class Solution:
    def mostPopularCreator(self, creat: List[str], ids: List[str], views: List[int]) -> List[List[str]]:
        d = defaultdict(int)
        h = defaultdict(list)
        for i in range(len(creat)):
        
            e = creat[i]
            
            d[e]+=views[i]
            h[e].append([ids[i],views[i]])
        m = float('-inf')
        for i in d:
            m = max(m,d[i])
        res = []
        # print(m)
        # print(d)
        # print(h)
        for i in d:
            if d[i]==m:
                # print(i,h[i])
                arr = h[i]
                arr.sort(key = lambda x : (-x[1],x[0]))
                # print(arr)
                res.append([i,arr[0][0]])
        return res
            # key = e+"-"+ids[i]
            # d[key]+=views[i]
#             d[e]+=views[i]
            
#             if e in h:
#                 if ids[i]<h[e]:
#                     d[e] = ids[i]
#             else:
#                 d[e] = ids[i]
        