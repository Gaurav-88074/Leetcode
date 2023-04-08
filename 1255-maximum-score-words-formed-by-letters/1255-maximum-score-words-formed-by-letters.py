class Solution:
    def maxScoreWords(self, words: List[str], letters: List[str], score: List[int]) -> int:
        
        value = defaultdict(int)
        for i in range(97,97+26):
            value[chr(i)] = score[i-97]
        # print(value)
        d = defaultdict(int,Counter(letters))
        
        def isFeasible(word):
            c =Counter(word)
            for i in c:
                if c[i]>d[i]:
                    return False
            return True
        def getSum(word):
            res=0
            for i in word:
                res+=value[i]
            return res
        def debit(word):
            for i in word:
                d[i]-=1
        def credit(word):
            for i in word:
                d[i]+=1
        def compute(i):
            if i==len(words):
                return 0
            take = 0
            skip = 0
            
            if isFeasible(words[i]):
                debit(words[i])
                take = getSum(words[i]) + compute(i+1)
                credit(words[i])
                
            skip = compute(i+1)
            return max(take,skip)
            
            
        return compute(0)
        