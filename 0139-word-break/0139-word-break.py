class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        d = set(wordDict)

        @lru_cache(None)
        def compute(x):
            if x == len(s):
                return True
            take = False
            # skip = 1 + compute(x + 1)

            for i in range(x, len(s)):
                if s[x:i+1] in d:
                    take = take or compute(i + 1)
                if take:
                    return True
                    # skip = min(skip, take)

            return take

        return compute(0)