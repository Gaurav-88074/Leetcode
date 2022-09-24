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
    //---------------------------------------------------
    private List<Integer> array = new ArrayList<>();
    private List<List<Integer>> res = new ArrayList<>();
    //---------------------------------------------------
    public void compute(TreeNode root,int target){
        // System.out.println(array.toString()+" -> "+target);
        if(root==null){
            // System.out.println(array.toString()+" -> "+target);
            return;
        }
        if(target-root.val==0 && root.left==null && root.right==null){
            array.add(root.val);
            res.add(new ArrayList<>(array));
            array.remove(array.size()-1);
            return;
        }
        array.add(root.val);
        compute(root.left ,target - root.val);
        compute(root.right,target - root.val);
        array.remove(array.size()-1);
        
    }
    public List<List<Integer>> pathSum(TreeNode root, int targetSum) {
        if(root==null){
            return new ArrayList<>();
        }
        
        compute(root,targetSum);
        
        return this.res;
    }
}
//     public boolean hasPath(TreeNode root,int targetSum,List<Integer> list){
//         if(targetSum==0 && root.left==null && root.right==null){
//             return true;
//         }
//         if(root==null){
//             return false;
//         }
        
//         boolean left = root.left !=null ? hasPath(root.left,targetSum-root.left.val,list)  : false;
//         boolean right= root.right!=null ? hasPath(root.right,targetSum-root.right.val,list) : false;
//         if(left||right){
//             list.add(root.val);
//         }
//         return left||right;
//     }