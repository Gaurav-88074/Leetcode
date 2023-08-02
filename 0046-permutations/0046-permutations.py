class Solution:
    def p(self,a, l, r,res):
        if l==r:
            # print(a)
            res.append([*a])
        else:
            for i in range(l,r):
                a[l], a[i] = a[i], a[l]
                self.p(a, l+1, r,res)
                a[l], a[i] = a[i], a[l] # backtrack
    def permute(self, nums):
        res =[]
        self.p(nums,0,len(nums),res)
        return res