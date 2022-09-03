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
    private ListNode lastGotAsHead = null; 
    private int maxSize;
    private ListNode v=null;
    public ListNode reverse(ListNode head,ListNode prev){
        if(head==lastGotAsHead){
            return head;
        }
        if(head.next==lastGotAsHead){
            head.next = prev;
            return head;
        }
        ListNode thisNode = head;
        head = reverse(head.next, thisNode);
        
        thisNode.next = prev;
        return head;
    }
    public ListNode compute(ListNode head,int size,int k){
        if(head==null){
            maxSize = size;
            //-----------------------
            return head;
        }
        if(size%k==0){
            v= head;
        }
        head.next = compute(head.next,size+1,k);
        //-------------------------------
        if(size%k==0 ){
            lastGotAsHead = reverse(head,lastGotAsHead);
            return lastGotAsHead;
        }
        return head;
        //--------------------------------
    }
    public ListNode reverseKGroup(ListNode head, int k) {
        ListNode temp = head;
        ListNode last=head;
        int index=1;
        while(temp!=null){
            if(index%k==0){
                last = temp;
            }
            index+=1;
            temp = temp.next;
        }
        ListNode addRemaining = last.next;
        last.next = null;
        //-------------------------
        ListNode res =  compute(head, 0 ,k);
        if(v==null){
            return res;
        }
        v.next = addRemaining;
        return res;
        
    }
}