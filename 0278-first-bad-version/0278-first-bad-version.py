# The isBadVersion API is already defined for you.
# @param version, an integer
# @return an integer
# def isBadVersion(version):

class Solution:
    def firstBadVersion(self, n):
        low = 1
        high= n
        
        while(low<high):
            version = (low+high)//2
            
            if isBadVersion(version):
                #checking whether its left is also bad
                if version-1>=1 and  isBadVersion(version-1):
                    high = version-1
                else:
                    return version
            else:
                low = version + 1
        return low
        