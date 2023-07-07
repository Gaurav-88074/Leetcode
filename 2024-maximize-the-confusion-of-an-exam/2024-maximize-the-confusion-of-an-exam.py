class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:
        true=0
        false=0
        index = 0
        res = 0
        
        for i,v in enumerate(answerKey):
            if v=="T":
                true+=1
            else:
                false+=1
            mn = min(true,false)
            while mn>k :
                ch = answerKey[index]
                index+=1
                if ch=="T":
                    true-=1
                else:
                    false-=1
                mn = min(true,false)
            # print(answerKey[index:i+1])
            res = max(res,i-index+1)
        return res