class Solution(object):
    def addBinary(self, a, b):
        a = int(a,2)
        b = int(b,2)
        return bin(a+b)[2:]
        """
        :type a: str
        :type b: str
        :rtype: str
        """
        