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
    private Stack<Integer> stack1 = new Stack<>();
    private Stack<Integer> stack2 = new Stack<>();
    private int carry = 0;
    
    public void go(ListNode head,Stack<Integer> stack){
        if(head==null){
            return;
        }
        go(head.next,stack);
        
        if(stack.isEmpty()==false){
            int value = stack.pop();
            
            head.val += value+carry;
            // System.out.println(value+" head.val = "+head.val);
        
            carry = head.val/10;
            head.val%=10;
        }
        else{
            head.val += carry;
            carry = head.val/10;
            head.val%=10;
        }
        
    }
    public ListNode addTwoNumbers(ListNode l1, ListNode l2) {
        ListNode head1 = l1;
        ListNode head2 = l2;
        
        while(head1!=null && head2!=null){
            
            stack1.push(head1.val);
            stack2.push(head2.val);
            
            head1 = head1.next;
            head2 = head2.next;
        }
        if(head1 == null){
            go(l2,stack1);
            if(carry!=0){
                ListNode head = new ListNode(carry);
                head.next = l2;
                return head;
            }
            return l2;
        }
        
        go(l1,stack2);
        if(carry!=0){
            ListNode head = new ListNode(carry);
            head.next = l1;
            return head;
        }
        
        return l1;
        // System.out.println(carry);
        // go(l1);
        // if(carry!=0){
        //     ListNode head = new ListNode(carry);
        //     head.next = l1;
        //     return head;
        // }
        // return l1;
    }
}