# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapPairs(self, head: Optional[ListNode]) -> Optional[ListNode]:
        # def reverse(head,prev,k):
        #     if head==None or k==2:
        #         return prev
        #     else:
        #         temp = prev
        #         res  = reverse(head.next,head,k+=1)
        #         head.next = temp
        #         return res
        # return reverse(head,None)
        #---------------------
        def compute(head,prev,i):
            if head==None:
                return head
            compute(head.next,head,i+1)
            if i%2==0 and prev!=None:
                prev.val,head.val = head.val,prev.val
        compute(head,None,1)
        return head
                
                
                