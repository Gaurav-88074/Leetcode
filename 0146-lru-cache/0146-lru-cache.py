class node:
    def __init__(self,key,val):
        self.key = key
        self.val = val
        self.left = None
        self.right= None
    def __str__(self):
        return "["+str(self.val)+"]"
class LRUCache:

    def __init__(self, capacity: int):
        self.d = dict()
        self.size = 0
        self.capacity = capacity
        self.head = None
        self.tail = None
    
    def append(self,newNode):
        if self.head==None:
            self.head = newNode
            self.tail = self.head 
        else:
            
            
            self.tail.right = newNode
            newNode.left = self.tail            
            self.tail = newNode

    def get(self, key: int) -> int:
        if key in self.d:
            value = self.d[key].val
            #----------------------
            thatNode = self.d[key]
            thatNode.val = value
            i_right = thatNode.right
            i_left  = thatNode.left
            if(i_right!=None and i_left!=None):
                i_right.left = thatNode.left
                i_left.right = thatNode.right
            elif(i_right==None and i_left!=None):
                i_left.right  = None
                self.tail = i_left

            elif(i_right!=None and i_left==None):
                i_right.left = None
                self.head = i_right
            else:
                self.head = None
                self.tail = None
            newNode = node(key,value)
            self.append(newNode)
            self.d[key] = newNode
            #----------------------
            return value
        return -1

    def put(self, key: int, value: int) -> None:
        # print(key,self.size)
        if self.size==self.capacity and key not in self.d:
            eliminate = self.head.key
            
            #-----------------------------
            thatNode = self.head
            i_right = thatNode.right
            i_left  = thatNode.left
            if(i_right!=None and i_left!=None):
                i_right.left = thatNode.left
                i_left.right = thatNode.right
            elif(i_right==None and i_left!=None):
                i_left.right  = None
                self.tail = i_left

            elif(i_right!=None and i_left==None):
                i_right.left = None
                self.head = i_right
            else:
                self.head = None
                self.tail = None
            #-----------------------------
            # print(eliminate,self.d)
            del self.d[eliminate]            
            # print(f"${eliminate} was deleted")
            newNode = node(key,value)
            self.d[key] = newNode
            self.append(newNode)
        else:
            if key in self.d:
                thatNode = self.d[key]
                thatNode.val = value
                i_right = thatNode.right
                i_left  = thatNode.left
                if(i_right!=None and i_left!=None):
                    i_right.left = thatNode.left
                    i_left.right = thatNode.right
                elif(i_right==None and i_left!=None):
                    i_left.right  = None
                    self.tail = i_left
                    
                elif(i_right!=None and i_left==None):
                    i_right.left = None
                    self.head = i_right
                else:
                    self.head = None
                    self.tail = None
                newNode = node(key,value)
                self.append(newNode)
                self.d[key] = newNode
            else:
                self.size+=1
                newNode = node(key,value)
                self.d[key] = newNode
                self.append(newNode)


# Your LRUCache object will be instantiated and called as such:
# obj = LRUCache(capacity)
# param_1 = obj.get(key)
# obj.put(key,value)
# 4 3 