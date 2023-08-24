class Solution:
    def fullJustify(self, words: List[str], mx: int) -> List[str]:
        n = len(words)
        res = []
        def compute(i):
            if i==n:
                return
            temp = []
            size=0
            while i<n and size + len(temp) +len(words[i]) <= mx:
                temp.append(words[i])
                size+=len(words[i])
                i+=1
            res.append(" ".join(temp))
            compute(i)
        compute(0)
        # print(res)
        ans = []
        for i in res[ : -1]:
            arr = i.split(" ")
            size= len(arr)
            space = mx-(len(i)-size+1)
            # print(i,space)
            div = len(arr)-1
            temp = [arr[0]]
            # print("div",2)
            for i in arr[1:]:
                if space%div==0:
                    x = space//div
                    temp.append(" "*x)
                    space-=x
                    # print(temp,x)
                else:
                    x = space//div
                    x+=1
                    temp.append(" "*x)
                    space-=x
                    # print(temp,x)
                temp.append(i)
                div-=1
            ans.append("".join(temp))
        ans.append(res[-1])
        
        res = []
        for i in ans:
            spaceNeed =mx-len(i)
            res.append(i+ " "*spaceNeed)
        return res