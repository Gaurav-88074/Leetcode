class Solution(object):
    def numberOfBeams(self, bank):
        st = []
        res =0
        for i in range(len(bank)):
            bank[i] = bank[i].count("1")
        # print(bank)
            v = bank[i]
            if len(st)==0 and v!=0:
                st.append(v)
            elif len(st)!=0 and v!=0:
                res+= (st[-1]*v)
                st.append(v)
        return res
        