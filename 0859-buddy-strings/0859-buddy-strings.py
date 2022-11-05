class Solution:
    def buddyStrings(self, s: str, goal: str) -> bool:
        if len(s)!=len(goal):return False
        check  =False
        h=defaultdict(int)
        first = False
        second=False
        a,b =None,None
        v=0
        for i in range(len(s)):
            # print(i,s[i]!=goal[i])
            if s[i]!=goal[i] and first==False:
                a =  s[i]
                b = goal[i]
                first=True
                v=1
            elif s[i]!=goal[i] and first==True and second==False:
                v=1
                c =  s[i]
                d = goal[i]
                if a==d and b==c:
                    second = True
                else:
                    # print("hit")
                    return False
            elif s[i]!=goal[i] and second==True:
                v=1
                return False
            if s[i]==goal[i]:
                # print(s[i])
                h[s[i]]+=2
                if h[s[i]]==4:
                    check = True
        return (check and v==0) or second