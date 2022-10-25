class Solution:
    def rangeSum(self, nums: List[int], n: int, left: int, right: int) -> int:
        prefix = []
        v = 0
        for i in nums:
            v+=i
            prefix.append(v)
        arr = []
        for i in range(n):
            for j in range(i,n):
                if i==0:
                    arr.append(prefix[j])
                else:
                    arr.append(prefix[j]-prefix[i-1])
        # print(arr)
        arr.sort()
        v = 0
        mod = 10**9 + 7
        for i in range(len(arr)):
            v+=arr[i]
            arr[i] = v
        if left==1:
            return arr[right-1]%mod
        return (arr[right-1]-arr[left-2])%mod