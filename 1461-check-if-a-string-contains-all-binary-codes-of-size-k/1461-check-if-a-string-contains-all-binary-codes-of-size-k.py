class Solution(object):
    def hasAllCodes(self, s, k):
        st = set()
        for i in range(len(s)-k+1):
            st.add( s[i:i+k] )
        # print(st)
        return len(st)==pow(2,k)
        