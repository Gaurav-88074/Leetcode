class Solution:
    def equalFrequency(self, word: str) -> bool:
        c = Counter(word)
        v = []
        arr = []
        for i in c:
            v.append(c[i])
            arr.append([i,c[i]])
        # print(c)
        # arr.sort(key = lambda x : x[1])
        # m = arr[0][1]
        m = min(v)
        
        
        cc = Counter(word)
        for i in cc:
            if cc[i]==m:
                cc[i]-=1
                break
        s = []
        for i in cc:
            if cc[i]!=0:
                s.append(cc[i])
        if len(set(s))==1 : return True
        #--------------------------
        cc = Counter(word)
        m = max(v)
        for i in cc:
            if cc[i]==m:
                cc[i]-=1
                break
        s = []
        for i in cc:
            if cc[i]!=0:
                s.append(cc[i])
        return len(set(s))==1
        
        
        