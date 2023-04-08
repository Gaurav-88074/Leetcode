"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""
#hashmappppppppppppp
class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        original = dict()
        duplicate= dict()
        def compute(head,index):
            if not head : return None
            
            copyHead = Node(head.val)
            #-----------------------------------------
            original[head] = index
            duplicate[index] = copyHead
            #----------------------------------------
            #------------------------------------
            copyHead.next = compute(head.next,index+1)
            #----------------------------------
            #-----------------------------------
            theirRandom = head.random
            if(theirRandom!=None):
                idx = original[theirRandom]
                itsRandom = duplicate[idx]
                copyHead.random = itsRandom
            else:
                copyHead.random==None
            return copyHead
        return compute(head,1)