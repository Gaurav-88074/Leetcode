class Solution:
    def checkArithmeticSubarrays(self, nums: List[int], l: List[int], r: List[int]) -> List[bool]:
        res = []
        for i in range(len(l)):
            left = l[i]
            right=r[i]
            
            st = set()
            
            subArray = nums[left :right+1]
            subArray.sort()
            for i in range(1,len(subArray)):
                st.add(subArray[i]-subArray[i-1])
            
            res.append(len(st)==1)
        return res