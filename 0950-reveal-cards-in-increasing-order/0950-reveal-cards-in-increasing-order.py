class Solution:
    def deckRevealedIncreasing(self, deck: List[int]) -> List[int]:
        deck.sort(reverse =True)
        d = deque()
        d.append(deck[0])
        for i in range(1,len(deck)):
            v = d.pop()
            d.appendleft(v)
            d.appendleft(deck[i])
            
        
        return d
        
        
            