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
        index = 0
        steps = 0
        c=0
        # while True:
        for i in instructions:
            # i = instructions[index]
            
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
            # print(x,y,head.data)
            # index+=1
            # index%=len(instructions)
            # steps+=1
            # print(x,y,steps)
            # if x==0 and y==0 : c+=1
            # if x==0 and y==0 and c>=2: return True 
            # if steps==(10*len(instructions)) :return False
        # print(x,y)
        return x==0 and y==0 or head.data!="N"