class Solution:
    def isPrefixString(self, s: str, words: List[str]) -> bool:
        
        l =set(accumulate(words))
        return s in l