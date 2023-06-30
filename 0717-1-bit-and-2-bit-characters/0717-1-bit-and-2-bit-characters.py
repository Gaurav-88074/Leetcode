class Solution:
    def isOneBitCharacter(self, bits: List[int]) -> bool:
        i = 0
        lastPair = -1
        while i<len(bits):
            if bits[i]==1:
                if i+1<len(bits):
                    lastPair = i+1
                    i+=2
                else:
                    # print("endgame",i)
                    return False
            else:
                i+=1
        # print(lastPair)
        return lastPair!=len(bits)-1