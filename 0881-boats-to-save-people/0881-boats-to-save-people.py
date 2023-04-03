class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()
        left = 0
        right=len(people) -1 
        res = 0
        # print(people)
        while left<=right:
            if people[left]+people[right]<=limit:
                res  += 1
                left += 1
                right-= 1
            else:
                res+=1
                right-=1
        # print(left,right)
        return res