class Solution:
    
    def compute(self,index,nums):
        
        if len(self.array)>=2:
            # print(self.array)
            if hash(tuple(self.array)) not  in self.present:
                self.present.add(hash(tuple(self.array)))
                self.res.append([*self.array])
        if index==len(nums):
            # print(self.array)
            return
            
            
        #----------------------------
        #take this element
        #----------------------------
        if (len(self.array)==0 or self.array[-1]<=nums[index]):
            
            self.array.append(nums[index])
            # if len(self.array)>=2:
            #     self.res.append([*self.array])
            self.compute(index+1,nums)
            self.array.pop()
        #----------------------------
        #skip this element
        #----------------------------
        while index+1 < len(nums) and nums[index]==nums[index+1]:
            index+=1
        self.compute(index+1,nums)
        
    def findSubsequences(self, nums):
        self.array = [ ]
        self.res = [ ]
        self.present = set()
        # nums.sort()
        self.compute(0,nums)
        return self.res
        