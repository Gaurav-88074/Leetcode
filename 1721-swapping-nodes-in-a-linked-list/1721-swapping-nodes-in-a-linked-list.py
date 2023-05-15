# Definition for singly-linked list.
# class ListNode(object):
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution(object):
    def swapNodes(self, head, k):
        d = [defaultdict(None)]
        temp = head
        i=1
        while temp!=None:
            d.append(temp)
            i+=1
            temp=temp.next
        d[k].val ,d[-k].val= d[-k].val ,d[k].val
        return head