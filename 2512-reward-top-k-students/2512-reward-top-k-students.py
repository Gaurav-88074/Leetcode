class Solution:
    def topStudents(self, positive_feedback: List[str], negative_feedback: List[str], report: List[str], student_id: List[int], k: int) -> List[int]:
        p = set(positive_feedback)
        neg = set(negative_feedback)
        
        d = defaultdict(int)
        
        s = dict()
        for i,v in enumerate(student_id):
            s[v] = report[i]
        
        for i in s:
            key = i
            value=s[i]
            value = value.split(" ")
            score = 0
            
            for w in value:
                if w in p:
                    score+=3
                elif w in neg:
                    score-=1
            d[key] = score
        # print(d)
        res = []
        for i in d:
            res.append([
                i,d[i]
            ])
        res.sort(key = lambda x : (x[1],-x[0]),reverse=True)
        return [i[0] for i in res ][:k]