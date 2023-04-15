# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def nodesBetweenCriticalPoints(self, head: Optional[ListNode]) -> List[int]:
        
        arr = []
        
        def compute(head,index,pre):
            if not head:
                return head
            nextNode = compute(head.next,index+1,head)
            if pre!=None and nextNode!=None:
                if head.val<pre.val and head.val<nextNode.val:
                    arr.append(index)
                if head.val>pre.val and head.val>nextNode.val:
                    arr.append(index)
            return head
        compute(head,0,None)
        # arr.sort()
        arr.reverse()
        # print(arr)
        if len(arr)<2:
            return [-1,-1]
        else:
            mn = float('inf')
            for i in range(1,len(arr)):
                mn = min(mn,arr[i]-arr[i-1])
            return [ mn ,  arr[-1]-arr[0]]