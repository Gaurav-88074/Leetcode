class Solution:
    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
        start = 0
        fuel = 0
        # costamount =0
        stationCovered = 0
        currentPosition =0
        
        visited = 0
        while visited<2*len(gas)-1: 
            visited+=1
            # print("we are at ",currentPosition,"with",stationCovered,"station covered")
            fuel = fuel + gas[currentPosition]
            #---------------------------------
            if stationCovered>=len(gas) : 
                return start 
            #----------------------------------
            while fuel-cost[currentPosition] <0 and start<currentPosition:
                 
                # print("problem occured at",currentPosition,"fuel=",fuel,\
                # "cost=",cost[currentPosition],"s=",start)
                 
                fuel-=abs(gas[start] - cost[start]) 
                
                # print("fuel at",currentPosition,fuel)
                
                start+=1 
                 
                stationCovered -= 1 
            #---------------------------------------------
            if fuel-cost[currentPosition]<0: 
                # print("new problem occured at",currentPosition,"fuel=",fuel,\
                # "cost=",cost[currentPosition],"s=",start)
                fuel = 0 
                stationCovered = 0 
                start+=1
            else: 
                stationCovered+=1
                fuel = fuel - cost[currentPosition]
            #---------------------------------------
            currentPosition+=1
            currentPosition%=len(gas)
            #---------------------------------------
            if stationCovered==len(gas) : 
                return start 
        return -1