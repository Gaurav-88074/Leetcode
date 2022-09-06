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
class value{
    public boolean hasOne;
    public value(boolean b){
        this.hasOne = b;
    }
}
class Solution {
    // private boolean hasOne;
    public TreeNode compute(TreeNode root,value obj){
        if(root==null){
            // hasOne = hasOne==true ? true : false;
            return root;
        }
        value newObj = new value(false);
        
        root.left = compute(root.left,newObj);
        root.right= compute(root.right,newObj);
        
        if(root.val==1 || newObj.hasOne==true){
            obj.hasOne = true;
            return root;
        }
        else{
            return null;
        }
       
        // return root;
    }
    public TreeNode pruneTree(TreeNode root) {
        value obj = new value(false);
        return compute(root,obj);
    }
}
// hasOne = hasOne || (root.val==1);
// if(hasOne==true || (root.val==1)){
//     hasOne=true;
//     return root;
// }
// else{
//     // System.out.println(root.val);
//     // if(root.left!=null) System.out.println("left = "+root.left.val);
//     // if(root.right!=null) System.out.println("right = "+root.right.val);
//     hasOne = false;
//     return null;
// }











