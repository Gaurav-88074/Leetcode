class Solution:
    def subdomainVisits(self, cpdomains: List[str]) -> List[str]:
        d = defaultdict(int)
        
        for domain in cpdomains:
            _id,url = domain.split(" ")
            
            _id = int(_id)
            url = url.split(".")
            
            subdomain = ""
            for i in range(len(url)-1,-1,-1):
                if len(subdomain)==0:
                    subdomain += url[i]
                else:
                    subdomain = url[i] + "." + subdomain
                d[subdomain]+=_id
        # print(d)
        res = []
        for key in d:
            value= d[key]
            # print(key,value)
            res.append(str(value)+" "+key)
        return res