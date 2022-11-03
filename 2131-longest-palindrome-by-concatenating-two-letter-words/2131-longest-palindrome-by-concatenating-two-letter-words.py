class Solution:
    def longestPalindrome(self, words: List[str]) -> int:
        c = Counter(words)
        res = 0
        m = 0
        case = False
        for w in c:
            rev = w[::-1]
            if w==rev:
                value = c[w]
                if value%2==0:
                    res+= (2*c[w])
                else:
                    res+= (value - (value%2))*2
                    case = True
            else:
                if rev in c:
                    res+=min(c[w],c[rev])*2
        if case : res+=2
        return res 