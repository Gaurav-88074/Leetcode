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
    private ListNode thatNode;
    private int maxSize;
    public void compute(ListNode head,int size,int k){
        if(head==null){
            maxSize = size;
            return;
        }
        if(size==k){
            thatNode = head;
        }
        compute(head.next,size+1,k);
        if(maxSize-size==k){
            int temp = head.val;
            head.val = thatNode.val;
            thatNode.val = temp;
        }
        //-------------------------------
        
    }
//     public ListNode fast(ListNode head, int k){
        
    // }
    public ListNode swapNodes(ListNode head, int k) {
        //it worked
        compute(head,1,k);
        return head;
    }
}