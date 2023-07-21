class Solution:
    def findOcurrences(self, text: str, first: str, second: str) -> List[str]:
        res = []
        text = text.split(" ")
        n = len(text)
        for i in range(0,n-2):
            if text[i]==first and text[i+1]==second:
                res.append(text[i+2])
        return res
        