class Solution(object):
    def longestCommonPrefix(self, strs):
        m = min([len(strs[i]) for i in range(len(strs))])
        # print(m)
        res = []
        for i in range(m):
            head = strs[0][i]
            flag = True
            for j in range(1,len(strs)):
                if strs[j][i]!=head:
                    flag = False
                    break
            if flag:
                res.append(head)
            else:
                break
        return "".join(res)
        