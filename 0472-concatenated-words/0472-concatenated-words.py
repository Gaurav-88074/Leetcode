class Solution:
    def findAllConcatenatedWordsInADict(self, words: List[str]) -> List[str]:
        s = set(words)
        
        # @lru_cache(None)
        def is_possible(word,index,char,count):
            if index==len(word):
                if char in s and count>0:
                    return True
                return False
            char+=word[index]
            if char in s: 
                if word[index+1: ] in s or is_possible(word,index+1,"",count+1):
                    return True
            return is_possible(word,index+1,char,count)
        res = []
        for i in words:
            if is_possible(i,0,"",0):
                res.append(i)
        return res