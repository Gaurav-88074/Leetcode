class Solution:
    def partitionString(self, s: str) -> int:
        st = set()
        res = 0
        for i in s:
            if i in st:
                res+=1
                # print(i)
                st =set()
            st.add(i)
        return res+1