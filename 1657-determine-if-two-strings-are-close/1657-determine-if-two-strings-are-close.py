class Solution:
    def closeStrings(self, word1: str, word2: str) -> bool:
        # print(Counter(word1).values(),Counter(word2).values())
        a = Counter(word1)
        b = Counter(word2)
        arr1 = []
        arr2 = []
        for i in a:
            arr1.append([
                i,a[i]
            ])
        for i in b:
            arr2.append([
                i,b[i]
            ])
        arr1.sort(key = lambda x : x[1])
        arr2.sort(key = lambda x : x[1])
        # print(arr1)
        # print(arr2)
        d = dict()
        for i in range(len(arr1)):
            d[arr1[i][0]] = i
            if arr1[i][1]!=arr2[i][1]:
                return False
        
        for i in range(len(arr1)):
            c1 = arr1[i][0]
            c2 = arr2[i][0]
            if c1!=c2 and c2 not in a:
                return False 
            elif c1!=c2 and c2 in a:
                thatIndex = d[c2]
                arr1[thatIndex][0] = c1
                
        return True