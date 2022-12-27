class Solution(object):
    def maximumBags(self, capacity, rocks, additionalRocks):
        arr = []
        v = additionalRocks
        n = len(rocks)
        for i in range(n):
            arr.append(capacity[i] - rocks[i])
        res = 0
        arr.sort()
        for i in arr:
            if v-i >=0:
                res+=1
                v-=i
            else:
                break
        return res
        