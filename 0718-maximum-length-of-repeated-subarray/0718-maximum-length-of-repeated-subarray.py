class Solution:
    def findLength(self, nums1: List[int], nums2: List[int]) -> int:
        strnum2 = ''.join(map(chr,nums2))
        strmax = ''
        ans = 0
        for num in nums1:
            strmax += chr(num)
            if strmax in strnum2:
                ans = max(ans,len(strmax))
            else:
                strmax = strmax[1:]
        return ans
#         @lru_cache(None)
#         def compute(m,n):
#             if m==len(nums1) or n==len(nums2) : 
#                 return 0
            
#             if nums1[m]==nums2[n] :
#                 return  1 + compute(m+1,n+1)
#             else:
#                 left  = compute(m+1,n)
#                 right = compute(m,n+1)

#                 res   = max(left,right)
#                 return res
#             # count = max(count,res)
#             # return res
#         return compute(0,0)