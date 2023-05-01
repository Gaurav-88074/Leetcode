class Solution:
    def average(self, salary: List[int]) -> float:
        a=min(salary)
        b=max(salary)
        s=sum(salary)
        s-=a
        s-=b
        return s/(len(salary)-2)