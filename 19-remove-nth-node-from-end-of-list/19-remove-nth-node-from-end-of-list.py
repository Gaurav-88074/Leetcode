# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def removeNthFromEnd(self, head, n):
        self.index = 0
        def get(head,size):
            if head==None:
                self.index = size-n
                return
            head.next = get(head.next,size+1);
            if self.index==size:
                return head.next;
            return head;
        return get(head,0);
        