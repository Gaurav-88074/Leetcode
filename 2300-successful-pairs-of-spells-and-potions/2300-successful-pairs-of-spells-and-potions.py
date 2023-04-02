class Solution(object):
    def binarySearch(self,potions,i,success):
        low = 0
        high= len(potions)-1
        # mid = None
        # print("-----------")
        while low<=high:
            # print(low,high)
            mid = (low+high)//2
            if( (potions[mid] * i) >=success):
                if mid==0:
                    return mid#logic is much required
                elif (mid-1>-1 and (potions[mid-1] * i) >=success):
                    high = mid-1
                else:
                    return mid-1
            else:
                if mid==len(potions)-1:
                    return mid
                elif(mid+1 < len(potions) and (potions[mid+1] * i) < success):
                    low = mid+1
                else:
                    return mid
        return mid
    def successfulPairs(self, spells, potions, success):
        potions.sort()
        res = []
        for i in spells:
            index = self.binarySearch(potions,i,success)
            if index==0 and potions[0]*i >=success:
                res.append(len(potions))
            elif index==len(potions) and potions[0]*i <success:
                res.append(0)
            else:
                p = len(potions)-(index+1)
                res.append(p)
        return res
                    
        