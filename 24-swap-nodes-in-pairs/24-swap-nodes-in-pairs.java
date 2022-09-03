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
    public ListNode swapPairs(ListNode head) {
        if(head==null||head.next==null){
            return head;
        }
        List<ListNode> l = new LinkedList<>();
        // l.add(null);
        ListNode temp = head;
        while(temp!=null){
            l.add(temp);
            temp = temp.next;
        }
        int t;
        int k = (l.size()&1)==0 ? l.size():l.size()-1; 
        for(int i =0 ; i< k ; i+=2){
            t = l.get(i).val;
            l.get(i).val  = l.get(i+1).val;
            l.get(i+1).val = t;
        }
        return head;
    }
}