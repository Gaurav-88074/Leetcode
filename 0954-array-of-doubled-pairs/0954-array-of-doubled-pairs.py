from sortedcontainers import SortedList,SortedDict
class Solution:
    def compute(self,nums):
        # print(nums)
        c = Counter(nums)
        c = SortedDict(c)
        # print(c)
        single= 0
        res = 0
        for i in c:
            if c[i]==0:continue
            v = c[i]
            friend = 2*i
            if friend in c:
                ff = c[friend]
                m = min(v,ff)
                c[friend]-=m
                res+=m
                single+=abs(m-v)
                # print(c)
            else:
                single+=c[i]
        return [single,res]
    def canReorderDoubled(self, arr: List[int]) -> bool:
        numsp =[]
        numsn =[]
        n = []
        shouldBe= len(arr)//2
        res = 0
        zero = 0
        for i in arr:
            if i<0:
                numsn.append(-i)
            elif i>0:
                numsp.append(i)
            else:
                zero+=1
        
        singlen,resn  = self.compute(numsn)
        singlep,resp  = self.compute(numsp)
        # print(single) 
        res = resp+resn 
        single = singlen + singlep 
        
        if res + (zero//2)==shouldBe:return True
#         if zero<single:return False
        
#         if zero>single and (zero-single)%2==0:return True
        
#         return zero==single
        
        # return shouldBe == zero + res
        
        