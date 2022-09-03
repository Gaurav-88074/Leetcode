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
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        // List<ListNode> l =  new ArrayList<>();
        
        int carry = 0;

        ListNode head = null;
        ListNode tail = null;
        ListNode temp = null;
        
        int sum;
        
        while(l2!=null && l1!=null){
            sum = l1.val + l2.val;
            sum+=carry;
            carry = sum>9  ? 1 : 0;
            sum = sum%10;
            // sum
            // l.add(sum);
            
            //-------------------------
            // head = add(head,tail,sum);
            if(head==null){
                head = new ListNode(sum);
                tail = head;
            }
            else{
                temp = tail;
                temp.next = new ListNode(sum);
                tail = temp.next;
            }
            l1 = l1.next;
            l2 = l2.next;
        }
        while(l1!=null){
            sum = l1.val;
            sum+=carry;
            carry = sum>9  ? 1 : 0;
            sum = sum%10;
            // sum
            // l.add(sum);
            temp = tail;
            temp.next = new ListNode(sum);
            tail = temp.next;
            
            l1 = l1.next;
        }
        while(l2!=null){
            sum = l2.val;
            sum+=carry;
            carry = sum>9  ? 1 : 0;
            sum = sum%10;
            // sum
            // l.add(sum);
            //-------------------------
            temp = tail;
            temp.next = new ListNode(sum);
            tail = temp.next;
            
            l2 = l2.next;
        }
        if(carry==1){
            temp = tail;
            temp.next = new ListNode(1);
            tail = temp.next;
            // l.add(1);
        }
        // System.out.println(l);
        return head;
        
        
    }
}