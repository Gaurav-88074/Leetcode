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
    public ListNode oddEvenList(ListNode head) {
        ListNode even = new ListNode();
        ListNode evenp= even;
        
        ListNode odd = new ListNode();
        ListNode oddp = odd;
        
        int index = 1;
        while(head!=null){
            if((index & 1)==1){
                oddp.next = head;
                oddp = oddp.next;
            }
            else{
                evenp.next = head;
                evenp = evenp.next;
            }
            head=head.next;
            index+=1;
        }
        even = even.next;
        odd  = odd.next;
        
        // System.out.println(evenp.val);
        // System.out.println(oddp.val);
        
        evenp.next = null;
        oddp.next = even;
        
        return odd;
    }
}