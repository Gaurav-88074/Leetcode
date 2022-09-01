class Solution:
    def maxUncrossedLines(self, nums1: List[int], nums2: List[int]) -> int:
        @lru_cache(None)
        def compute(index1,index2):
            if(index1==-1 or index2==-1) :  return 0
            
            elif(nums1[index1]==nums2[index2]):
                return 1 + compute(index1-1,index2-1)
            else:
                left = compute(index1-1,index2)
                right= compute(index1,index2-1)
                return max(left,right)
        return compute(len(nums1)-1,len(nums2)-1)