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
    public TreeNode add(TreeNode root,int val,int depth,int levelIndex,int child){
        if(root==null){
            if(levelIndex==depth){
                return new TreeNode(val);
            }
            else{
                return root;
            }
        }
        if(levelIndex==depth){
            // System.out.println("Spotted "+root.val);
            //-----------------------------------
            // TreeNode newChild = new TreeNode(val);
            if(child==-2){
                // newChild.left  = root;
                return new TreeNode(val,root,null);
            }
            else{
                // newChild.right = root;
                return new TreeNode(val,null,root);
            }
            // return newChild;
            //-----------------------------------
        }
        root.left  = add(root.left ,val,depth,levelIndex+1,-2);
        root.right = add(root.right,val,depth,levelIndex+1,2);
        return root;
        
    }
    public TreeNode addOneRow(TreeNode root, int val, int depth) {
        if(depth==1){
            return new TreeNode(val,root,null);
        }
        return add(root,val,depth,1,0);
    }
}