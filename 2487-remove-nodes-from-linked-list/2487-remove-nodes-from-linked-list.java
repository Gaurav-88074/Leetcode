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
    public ListNode compute(ListNode head){
        if(head==null){
            return head;
        }
        head.next = compute(head.next);
        if(head.next!=null && head.next.val>head.val){
            return head.next;
        }
        return head;
    }
    public ListNode removeNodes(ListNode head) {
        return compute(head);
    }
}