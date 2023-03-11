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
/**
 * Definition for a binary tree node.
 * public class TreeNode {
 *     int val;
 *     TreeNode left;
 *     TreeNode right;
 *     TreeNode() {}
 *     TreeNode(int val) { this.val = val; }
 *     TreeNode(int val, TreeNode left, TreeNode right) {
 *         this.val = val;
 *         this.left = left;
 *         this.right = right;
 *     }
 * }
 */
class Solution {
    public TreeNode buildBST(ListNode head){
        if(head==null){
            return null;
        }
        if(head.next==null){
            return new TreeNode(head.val);
        }
        ListNode start  = head;
        ListNode mid    = head;
        ListNode midPre = mid;
        //-----------------------------------
        while(start!=null && start.next!=null ){
            start = start.next.next;
            midPre = mid;
            mid   = mid.next;
        }
        // System.out.println(mid.val);
        //-------------------------------------
        midPre.next =null;
        //-------------------------------------
        TreeNode root = new TreeNode(mid.val);
        //-------------------------------------
        root.left  = buildBST(head);
        root.right = buildBST(mid.next);
        //-------------------------------------
        
        return root;
    }
    public TreeNode sortedListToBST(ListNode head) {
        
        return buildBST(head);
    }
}
//this also works
// class Solution {
//     public TreeNode toBST(List<Integer> array,int low,int high){
//         if(low>high){
//             return null;
//         }
//         int mid = (low+high)/2;
        
//         TreeNode root = new TreeNode(array.get(mid));
//         root.left  = toBST(array,low,mid-1);
//         root.right = toBST(array,mid+1,high);
//         return root;
//     }
//     public TreeNode sortedListToBST(ListNode head) {
//         List<Integer> array  = new ArrayList<>();
//         while(head!=null){
            
//             array.add(head.val);
//             head = head.next;
//         }
//         return toBST(array,0,array.size()-1);
//     }
// }