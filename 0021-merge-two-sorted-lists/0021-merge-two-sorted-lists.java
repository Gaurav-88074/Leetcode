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
    public ListNode mergeTwoLists(ListNode head1, ListNode head2) {
        if (head1==null){
        return head2;
    }
    else if (head2==null){
        return head1;
    }
    else if(head1.val<head2.val){
        head1.next = mergeTwoLists(head1.next,head2);
    }
    else{
        head2.next = mergeTwoLists(head2.next,head1);
    }
    return head1.val<head2.val?head1:head2;
    }
}