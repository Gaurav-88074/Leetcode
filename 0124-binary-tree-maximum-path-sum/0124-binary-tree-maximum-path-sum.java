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
class Pair{
    public int left;
    public int mid;
    public int right;
    public Pair(){
        this.left = 0;
        this.mid  = 0;
        this.right= 0;
    }
    public Pair(int a,int m,int b){
        this.left = a;
        this.mid  = a;
        this.right= b;
    }
}
class Solution {
    int max = Integer.MIN_VALUE;
    
    public int maxPathSum(TreeNode root) 
    {
        // O(n) time | O(h) space
        DFS(root);
        
        return max;
    }
    
    private int DFS(TreeNode root)
    {
        if(root == null)    return 0;
        
        int left = Math.max(DFS(root.left), 0);
        int right = Math.max(DFS(root.right), 0);
        
        int cur = root.val + left + right;
        
        max = Math.max(cur, max);
        
        return root.val + Math.max(left, right);
    }
}