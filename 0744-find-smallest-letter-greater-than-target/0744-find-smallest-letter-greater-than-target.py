class Solution(object):
    def nextGreatestLetter(self, letters, target):
        
        low = 0
        high =len(letters)-1
        if letters[-1]<=target:
            return letters[0]
        while (low<high):
            mid = (low+high)//2
            
            if letters[mid]<=target:
                low  = mid+1
            else:
                high = mid
        # print(high)
        return letters[high]
        