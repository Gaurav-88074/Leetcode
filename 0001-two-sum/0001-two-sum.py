class Solution(object):
    def twoSum(self, nums, target):
        d = defaultdict(set)
        for i in range(len(nums)):
            d[nums[i]].add(i)
        index =0
        for i in nums:
            check = target - i
            v = d[check]
            if len(v)!=0:
                if check==i and len(v)>=2:
                    # print("1")
                    second = v.pop()
                    while second==index: second  = v.pop()
                    return [index,second]
                elif (check!=i):
                    # print("2")
                    # print(i,check)
                    return [index,v.pop()]
            index+=1
        return []
        
                    
        
        
        