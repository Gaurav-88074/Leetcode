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
    public int[] inorder;
    public int[] postorder;
    public HashMap<Integer,Integer> map = new HashMap<>();
    public int ip;
    public TreeNode compute(int start,int end){
        //Base condition by he who remains
        if(start>end || ip<0){
            return null;
        }
        //------------------------
        int value = postorder[ip];
        ip = ip - 1;
        int mid = map.get(value);
        //------------------------
        TreeNode node  = new TreeNode(value);
        node.right = compute(mid + 1, end);
        node.left  = compute(start , mid - 1);
        //------------------------
        return node;
    }
    public TreeNode buildTree(int[] inorder, int[] postorder) {
        //------------------------------
        this.inorder   = inorder;
        this.postorder = postorder;
        this.ip = inorder.length-1;
        //------------------------------
        for(int i = 0; i < inorder.length ; i++){
            map.put(inorder[i],i);
        }
        //------------------------------
        int start = 0;
        int end   = inorder.length-1;
        //------------------------------
        return compute(start,end);
    }
}