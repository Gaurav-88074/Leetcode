class Node:
    def __init__(self, data):
        self.data = data
        self.next = None
        self.prev = None

class Solution:
    def isRobotBounded(self, instructions: str) -> bool:
        x = 0
        y = 0
        
        north = Node("N")
        west  = Node("W")
        south = Node("S")
        east  = Node("E")
        #------------------
        north.next = east
        north.prev = west
        
        east.prev  = north
        east.next  = south
        
        south.prev = east
        south.next = west
        
        west.prev  = south
        west.next  = north
        
        
        #------------------
        head = north;
        #------------------
        
        for i in instructions:
            
            
            if i=="L":
                head=head.prev
            elif i=="R":
                head = head.next
            else:
                if head.data == "N":
                    y+=1
                if head.data == "S":
                    y-=1
                if head.data == "E":
                    x+=1
                if head.data == "W":
                    x-=1
            
        return x==0 and y==0 or head.data!="N"