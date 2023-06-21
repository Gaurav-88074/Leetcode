class Solution:
    def minCost(self, nums: List[int], cost: List[int]) -> int:
        def compute(arr,value):
            res = 0
            for i,cost in arr:
                m = abs(value-i)
                res+=(m*cost)
            return res
        arr = []
        for i in range(len(nums)):
            arr.append(
                [
                    nums[i],
                    cost[i]
                ]
            )
        # arr.sort(key = lambda x : x[0])
        # print(arr)
        low = min(nums)
        high= max(nums)
        res = 0
        while low<high:
            mid1 = (low+high)//2
            mid2 = mid1+1
            
            c1 = compute(arr,mid1)
            c2 = compute(arr,mid2)
            if  c1<c2:
                res = c1
                high= mid1
            else:
                res = c2
                low = mid2
        return res
                
            