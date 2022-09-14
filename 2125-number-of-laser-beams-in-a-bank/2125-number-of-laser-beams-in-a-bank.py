class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        for i in range(len(bank)):
            bank[i] = bank[i].count("1")
        # print(bank)
        st = []
        res =0
        for i in bank:
            if len(st)==0 and i!=0:
                st.append(i)
            elif len(st)!=0 and i!=0:
                res+= (st[-1]*i)
                st.append(i)
        
        return res