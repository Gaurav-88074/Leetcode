class Solution(object):
    def averageValue(self, nums):
        arr = []
        for i in nums:
            if i%2==0 and i%3==0:
                arr.append(i)
        if len(arr)==0:return 0
        return sum(arr)/len(arr)
        