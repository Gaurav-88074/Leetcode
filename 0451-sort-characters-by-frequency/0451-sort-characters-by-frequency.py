class Solution:
    def frequencySort(self, s: str) -> str:
        l = list(s)
        h = [0] * 123
        for i in l:
            h[ord(i)]+=1
        temp = []
        for i in range(123):
            if h[i]!=0:
                temp.append( [chr(i),h[i] ])
        # print(temp)
        temp.sort(key = lambda x : x[1] , reverse = True)
        # temp.reverse()
        res = ""
        for i in temp:
            res+=i[0]*i[1]
        return res