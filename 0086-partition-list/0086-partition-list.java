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
    ListNode smallerNodesList = null;
    ListNode lastNode = null;
    
//     ListNode lastNode = null;
    // public ListNode addAtLast(ListNode head,ListNode addThis){
    //     if(head==null) return addThis;
    //     head.next = addAtLast(head.next,addThis);
    //     return head;
    // }
    public ListNode createFirstHalf(ListNode head,int x){
        if(head==null) return head;
        
        head.next = createFirstHalf(head.next,x);
        if(head.val < x){
            ListNode resAns = head.next;
            
            //-------------------------
            if(smallerNodesList==null){
                lastNode = head;
            }
            head.next = smallerNodesList;
            smallerNodesList = head;
            //-------------------------
            
            return resAns;
        }
        return head;
    }
    public ListNode partition(ListNode head, int x) {
        if(head==null) return null;
        ListNode temp  = head;
        
        temp = createFirstHalf(temp,x);
        // return smallerNodesList.next;
        if(smallerNodesList == null){
            return head;
        }
        else{
            lastNode.next = temp;
            return smallerNodesList;
            // return addAtLast(smallerNodesList,temp);
        }
        
    }
}