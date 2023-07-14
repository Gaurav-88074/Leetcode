class Solution:
    def longestSubsequence(self, arr: List[int], d: int) -> int:
        hashmap=defaultdict(int)
        res = 0
        for i in arr:
            
            value = hashmap[i-d]
            hashmap[i] = 1 + value
            
            res = max(res,hashmap[i])
        return res
#         n = len(arr)
        
#         @lru_cache(None)
#         def compute(index):
#             if index==n:
#                 return 0
#             res = 0
#             if index==None:
#                 for i in range(n):
#                     v = 1 + compute(i)
#                     res = max(res,v)
#             else:
#                 for i in range(index+1,n):
#                     # print("happend",arr[i],arr[pre])
#                     if arr[i]-arr[index]==d:
#                         # print("happend",arr[i],arr[pre])
#                         v = 1 + compute(i)
#                         res = max(res,v)
#             return res
#         return compute(None)