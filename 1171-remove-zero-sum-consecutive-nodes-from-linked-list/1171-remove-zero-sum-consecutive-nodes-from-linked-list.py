# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeZeroSumSublists(self, head: Optional[ListNode]) -> Optional[ListNode]:
        s= set([0])
        stack = []
        sumv=0
        while head!=None:
            sumv+=head.val
            stack.append([head.val,sumv])
            if sumv in s:
                obj = stack.pop()
                s.discard(obj[1])
                while len(stack)!=0 and stack[-1][1]!=sumv:
                    obj = stack.pop()
                    s.discard(obj[1])
            s.add(sumv)
            head=head.next
        
        def get(stack,i):
            if i==len(stack):return None
            newHead = ListNode(stack[i][0])
            newHead.next = get(stack,i+1)
            return newHead
            
        return get(stack,0)