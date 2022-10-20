class Solution:
    def intToRoman(self, num: int) -> str:
        def binarySearch(array,start,end,target):
            mid = (start+end)//2
            if start>end:
                return [
                    array[end],
                    array[start]
                ]
            if array[mid]==target:
                return [
                    array[mid]
                ]
            elif target<array[mid]:
                return binarySearch(array,start,mid-1,target)
            else:
                return binarySearch(array,mid+1,end,target)
        array = [1 ,5, 10, 50, 100, 500, 1000]
        sett = set(array)
        hashMap = {
            1   :"I",
            5   :"V",
            10  :"X",
            50  :"L",
            100 :"C",
            500 :"D",
            1000:"M"
        }
        values = [ ]
        div = 10
        m = 1
        while num>0:
            if num%div!=0 : values.append((num%div) * m)
            m*=10
            num//=10
        values.reverse()
        #-------Testing----------
        # print(values)
        # print(binarySearch(array,0,len(array)-1,58))
        res = []
        for i in values:
            #------------------
            if i>1000 and  i%1000 == 0:
                res.append((i//1000) * "M")
                continue
            #------------------
            present= i
            search = binarySearch(array,0,len(array)-1,present)
            if present - search[0]!=0 and search[1] - present in sett:#hashMap
                    res.append(hashMap[(search[1] - present)] + hashMap[search[1]])
                    continue
            res.append(hashMap[search[0]])
            while present-search[0]!=0:
                present-=search[0]
                search = binarySearch(array,0,len(array)-1,present)
                if present - search[0]!=0 and search[1] - present in sett:#hashMap
                    res.append(hashMap[(search[1] - present)] + hashMap[search[1]])
                    break
                
                res.append(hashMap[search[0]])
        
        # print(res)
        return "".join(res)