class Solution:
    def restoreIpAddresses(self, s: str) -> List[str]:
        res = [ ]
        arr = ["."]
        def compute(index,value,dot):
            # print(arr,value)
            if index==len(s) and dot!=3:
                return
            if index==len(s) and dot==3: 
                # print(arr)
                newArr = list(map(str,arr))
                v  ="".join(newArr[1:])
                res.append(v)
                # print(v)
                return
            c = int(s[index])
            # if c==0 and value
            upnext = value * 10 + c 
            # arr.append(c)
            if upnext>255 and dot<3:
                arr.append(".")
                arr.append(c)
                compute(index+1 , c,dot+1)
                arr.pop()
                arr.pop()
                
            elif upnext<=255:
                #------------------------
                # case 1
                if len(arr)!=1 and dot<3:
                    arr.append(".")
                    arr.append(c)
                    compute(index+1,c,dot+1)
                    arr.pop()
                    arr.pop()
                #-------------------------
                #case2
                if len(arr)>=2 and arr[-2]=="." and arr[-1]==0:
                    return
                
                arr.append(c)
                compute(index+1,upnext,dot)
                arr.pop()
                #-------------------------
                
        compute(0,0,0)
        return res
            
            
            