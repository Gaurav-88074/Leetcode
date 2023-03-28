class Solution:
    def originalDigits(self, s: str) -> str:
        # if (c == 'z') count[0]++;
        # if (c == 'w') count[2]++;
        # if (c == 'x') count[6]++;
        # if (c == 's') count[7]++; //7-6
        # if (c == 'g') count[8]++;
        # if (c == 'u') count[4]++; 
        # if (c == 'f') count[5]++; //5-4
        # if (c == 'h') count[3]++; //3-8
        # if (c == 'i') count[9]++; //9-8-5-6
        # if (c == 'o') count[1]++; //1-0-2-4
        num = {0:'zero',2:'two',6:'six'
               ,7:'seven',8:'eight',4:'four'
               ,5:'five',3:'three',9:'nine',
                1:'one'
              }
        res=[]
        def isFeasible(d,word):
            for i in word:
                if i not in d or d[i]==0:
                    return False
            return True
        def howMuch(d,word):
            res = float('inf')
            for i in word:
                res = min(res,d[i])
            for i in word:
                d[i]-=res
            # print(d)
            return res
        d = defaultdict(int)
        for i in s:
            d[i]+=1
        esv=[]
        for i,w in num.items():
            # w = num[i]
            if isFeasible(d,w):
                count = howMuch(d,w)
                esv.append([str(i) ,count])
        # print(esv)
        esv.sort(key = lambda x:x [0])
        for x,y in esv:
            res.append(x*y)
        return "".join(res)