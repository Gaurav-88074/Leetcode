class Solution(object):
    def findLongestChain(self, pairs):
        pairs.sort(key = lambda x : x[1])
        c = 1
        pre = pairs[0]
        res = 0
        # print(pairs)
        for i in range(1,len(pairs)):
            if pairs[i][0] > pre[1]:
                c+=1
                pre = pairs[i]
        #     else:
        #         res = max(res,c)
        #         c=1
        #         pre = pairs[i]
        # res = max(res,c)
        return c
        