class Solution:
    def largestAltitude(self, gain: List[int]) -> int:
        res = [0]
        for i in gain:
            m = i + res[-1]
            res.append(m)
        # print(res)
        return  max(res)