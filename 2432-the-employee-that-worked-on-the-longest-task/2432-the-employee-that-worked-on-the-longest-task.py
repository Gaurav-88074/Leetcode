class Solution:
    def hardestWorker(self, n: int, logs: List[List[int]]) -> int:
        temp = [0]
        for i in logs:
            temp.append(i[1])
        emp = [0]*n
        pre = 0
        for i in logs:
            _id,time = i
            emp[_id] = max(emp[_id],time-pre)
            pre = time
        # print(emp)
        # if n >100:
        #     print(emp[100])
        #     print(emp[221])
        res = 0
        v = emp[0]
        for i in range(1,n):
            if emp[i]>v:
                v = emp[i]
                res = i
        return res