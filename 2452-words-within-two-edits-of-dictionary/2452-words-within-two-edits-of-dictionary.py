class Solution(object):
    def twoEditWords(self, q, d):
        res = []
        def ans(i):

            for j in d:
                # c = Counter(i)
                z = 0
                for k in range(len(j)):
                    if j[k]!=i[k]:
                        z+=1
                if z<=2:
                    res.append(i)
                    return
                    
        for i in q:
            ans(i)
        return res
            
                    
        
        