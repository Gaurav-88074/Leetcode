class Solution(object):
    def findLength(self, nums1, nums2):
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
        