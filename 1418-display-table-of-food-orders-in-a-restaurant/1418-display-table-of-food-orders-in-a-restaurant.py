class Solution:
    def displayTable(self, orders: List[List[str]]) -> List[List[str]]:
        d = dict()
        st = set()
        tn = set()
        for order in orders:
            user,table,dish = order
            
            table = int(table)#imp step
            
            st.add(dish)
            tn.add(table)
            if table in d:
                d[table][dish]+=1
            else:
                d[table] = defaultdict(int)
                d[table][dish]+=1
        # print(d)
        dishes = list(st)
        tables = list(tn)
        
        dishes.sort()
        tables.sort()
        
        res = []
        
        firstRow = ["Table"]
        for dish in dishes:
            firstRow.append(dish)
        # print(firstRow)
        res.append(firstRow)
        
        for table in tables:
            hmap = d[table]
            
            dataRow=[0] * (len(dishes)+1)
            dataRow[0] = table
            # print(dataRow)
            for i in range(1,len(dishes)+1):
                dataRow[i]+=hmap[dishes[i-1]]
                
            for i in range(0,len(dataRow)):
                dataRow[i] = str(dataRow[i])
            res.append(dataRow)
        # print(res)
        return res
        
        