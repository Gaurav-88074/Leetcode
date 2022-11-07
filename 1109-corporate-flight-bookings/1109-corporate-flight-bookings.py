class Solution:
    def corpFlightBookings(self, bookings: List[List[int]], n: int) -> List[int]:
        res = [0]*n
        for a,b,c in bookings:
            a-=1
            b-=1
            res[a] += c
            if b+1<n:
                res[b+1] += -c
        v =0
        # print(res)
        for i in range(n):
            v+=res[i]
            res[i]=v
        return res