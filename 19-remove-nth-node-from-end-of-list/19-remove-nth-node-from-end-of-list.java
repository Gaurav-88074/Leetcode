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
    public ListNode removeNthFromEnd(ListNode head, int n) {
        List<ListNode> l = new ArrayList<>();
        ListNode temp = head;
        while(temp!=null){
            l.add(temp);
            temp = temp.next;
        }
        if(l.size()==1){
            return null;
        }
        if(n==l.size()){
            // head = head
            return head.next;
        }
        int index = l.size() - n-1;
        l.get(index).next = l.get(index+1).next;
        return head;
    }
}