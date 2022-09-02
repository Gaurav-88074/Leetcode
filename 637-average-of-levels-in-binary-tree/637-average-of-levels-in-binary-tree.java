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
    public List<Double> averageOfLevels(TreeNode root) {
        if(root==null) {
            return new ArrayList<>();
        }
        if(root.left==null && root.right==null){
            List<Double> res = new LinkedList<>();
            res.add((double)root.val);
            return res;
        }
        Queue<TreeNode> q = new LinkedList<>();
        List<Double> res = new LinkedList<>();
        long sum = 0;
        int nodes = 0;
        q.add(root);
        q.add(null);
        TreeNode head;
        // List<Integer> l = new LinkedList<>();
        while(q.isEmpty()==false){
            head = q.poll();
            if(head!=null){
                // System.out.print(head.val);
                // l.add(head.val);
                sum+=head.val;
                nodes+=1;
                if(head.left!=null){
                    q.add(head.left);
                }
                if(head.right!=null){
                    q.add(head.right);
                }
            }
            else{
                // System.out.println();
                res.add((double)sum/nodes);
                sum = 0;
                nodes = 0;
                // l = new LinkedList<>();
                if(q.isEmpty()==false){
                    q.add(head);
                }
            }
        }
        return res;
    }
}