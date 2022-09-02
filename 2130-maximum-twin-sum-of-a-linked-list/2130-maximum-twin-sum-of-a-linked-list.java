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
    public ListNode h = null;
    public int res = 0;
    public void compute(ListNode head){
        if(head==null){
            return;
        }

        compute(head.next);
        
        res = Math.max(res,head.val + h.val);
        
        h = h.next;
        
        
    }
    public int pairSum(ListNode head) {
        h = head;
        compute(head);
        return res;
    }
}