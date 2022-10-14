/**
 * Definition for singly-linked list.
 * public class ListNode {
 *     int val;
 *     ListNode next;
 *     ListNode() {}
 *     ListNode(int val) { this.val = val; }
 *     ListNode(int val, ListNode next) { this.val = val; this.next = next; }
 * }
 */
class Solution {
    public ListNode deleteMiddle(ListNode head) {
        if(head.next==null){
            return null;
        }
        ListNode p1 =head;
        ListNode p2 =head;
        ListNode res=head;
        while(p2!=null && p2.next!=null){
            res = p1;
            p1 = p1.next;
            p2 = p2.next.next;
        }
        res.next = res.next.next;
        return head;
    }
}