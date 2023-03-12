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
    public ListNode mergeKLists(ListNode[] lists) {
        
        ListNode res = null;
        ListNode last=res;
        Queue<Integer> pq = new PriorityQueue<>();
        for(ListNode head : lists){
            ListNode temp = head;
            while(temp!=null){
                pq.add(temp.val);
                temp = temp.next;
            }
        }
        while(!pq.isEmpty()){
            if(last==null){
                res = new ListNode(pq.poll());
                last = res;
            }
            else{
                ListNode toAdd = new ListNode(pq.poll());
                last.next = toAdd;
                last = last.next;
            }
            
            // last = last.next;
        }
        return res;
    }
}