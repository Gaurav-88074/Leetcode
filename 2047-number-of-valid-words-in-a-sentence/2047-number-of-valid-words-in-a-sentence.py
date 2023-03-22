class Solution:
    def countValidWords(self, sentence: str) -> int:
        arr = sentence.split(" ")
        # for i in range(len(arr)):
        #     arr[i] = arr[i].strip()
        st = {chr(i) for i in range(97,97+26)}
        # print(arr)
        res=0
        for w in arr:
            if w.strip()=="":
                continue
            #--------------------
            v=True
            hCount = 0
            pCount = 0
            #--------------------
            for i,c in enumerate(w):
                #-------------------------
                if c=='-' and i-1>=0\
                    and i+1<len(w) and\
                    w[i-1] in st and w[i+1] in st \
                    and hCount==0:
                    
                    hCount+=1
                    continue
                #-------------------------
                if (c=='!' or c=='.' or c==',') and i==len(w)-1:
                    continue
                #_------------------------
                if c in st:
                    continue
                #-------------------------
                #else case
                v=False
                break
            if v:
                # print(w)
                res+=1
        return res