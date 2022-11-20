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
    TreeSet<Integer> set = new TreeSet<>();
    public void inorder(TreeNode root){
        if(root==null){
            return;
        }
        inorder(root.left);
        set.add(root.val);
        inorder(root.right);
        
    }
    public List<List<Integer>> closestNodes(TreeNode root, List<Integer> queries) {
        inorder(root);
        List<List<Integer>> res = new ArrayList<>();
        for(int i : queries){
            Integer min = set.floor(i);
            Integer max = set.ceiling(i);
            List<Integer> t = new ArrayList<>();
            if(min==null){
                min=-1;
            }
            if(max==null){
                max = -1;
            }
            t.add(min);
            t.add(max);
            res.add(t);
        }
        return res;
        
    }
}