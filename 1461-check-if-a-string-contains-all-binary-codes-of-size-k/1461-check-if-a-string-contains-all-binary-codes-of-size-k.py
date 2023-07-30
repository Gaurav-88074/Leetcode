class Solution:
    def hasAllCodes(self, s: str, k: int) -> bool:

        st = set()
        for i in range(len(s)-k+1):
            st.add( s[i:i+k] )
        # print(st)
        return len(st)==pow(2,k)