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
    public void inOrder(TreeNode root,List<Integer> l){
        if(root==null)return;
        inOrder(root.left,l);
        l.add(root.val);
        inOrder(root.right,l);
    }
    public List<Integer> getAllElements(TreeNode root1, TreeNode root2) {
        List<Integer> nodes1 = new ArrayList<>();
        List<Integer> nodes2 = new ArrayList<>();
        inOrder(root1,nodes1);
        inOrder(root2,nodes2);
        
        List<Integer> ans = new ArrayList<Integer>();
        int i1 = 0;
        int i2 = 0;
        while (i1 < nodes1.size() && i2 < nodes2.size()){
            int val1 = nodes1.get(i1);
            int val2 = nodes2.get(i2);
            if (val1 == val2){
                ans.add(val1);
                ans.add(val2);
                i1++;
                i2++;
            }
            else if (val1 < val2){
                ans.add(val1);
                i1++;
            }
            else{
                ans.add(val2);
                i2++;
            }
        }
        
        while (i1 < nodes1.size())
            ans.add(nodes1.get(i1++));
        while (i2 < nodes2.size())
            ans.add(nodes2.get(i2++));
        
        return ans;
        
    }
}