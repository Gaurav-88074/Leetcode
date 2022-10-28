class Solution:
    def ordSum(self,s):
        # return hash(s)
        d = [0]*26
        for i in s:
            d[ord(i)-97]+=1
        return hash(tuple(d))
        # res = 0
        # for i in s:
        #     res+= ord(i)
        # return res 
    def groupAnagrams(self, strs):
        d=dict()
        for i in strs:
            v = self.ordSum(i)
            if v in d:
                d[v].append(i)
            else:
                d[v] = [i]
        # print(d)
        res =[]
        for i in d.values():
            res.append(i)
        return res