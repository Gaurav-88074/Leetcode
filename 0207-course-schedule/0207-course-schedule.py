class Solution:
    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
        graph = defaultdict(list)
        # 10 [0]
        # 18 [3]
        # 5  [5]
        # 11 [6]
        # 14 [11]
        # 1  [13]
        # 1  [15]
        # 4  [17]
        #--------------------------
        for a,b in prerequisites:
            graph[b].append(a)
        #--------------------------
        d = dict()
        def hasCycle(node):
            if node in d : 
                return d[node]
            d[node] = False
            for nei in graph[node]:
                ch = hasCycle(nei)
                if ch==False:
                    return False
            d[node] = True
            return True
        for i in range(numCourses):
            if hasCycle(i)==False:
                return False
        return True