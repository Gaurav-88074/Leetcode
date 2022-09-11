class Solution:
    def mostFrequentEven(self, nums: List[int]) -> int:
        v = []
        for i in nums:
            if i%2==0:
                v.append(i)
        if len(v)==0:return -1
        c = Counter(v)
        m = max(list(c.values()))
        arr=[]
        for i in c:
            if c[i]==m:
                arr.append(i)
        arr.sort()
        
        
        
        return arr[0]