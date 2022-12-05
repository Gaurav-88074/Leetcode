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
    public ListNode middleNode(ListNode head) {
        ListNode last = head;
        ListNode mid = head;
        while (last!=null){
            
        
            if (last.next==null){
                return mid;
            }
            last = last.next.next;
            mid = mid.next;
        }
        return mid;
    }
}