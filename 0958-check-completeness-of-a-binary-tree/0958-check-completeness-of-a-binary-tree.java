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
    public Integer[] map = new Integer[100];
    public int[] count = new int[100];
    public int maxLevel = 0;
    public boolean compute(TreeNode root,int level,int value){
        if(root==null)return true;
        
        count[level]+=1;
        maxLevel = Math.max(maxLevel,level);
        if(map[level]==null || map[level]!=value) return false;
        
        map[level] = value+1;
        
        boolean left  = compute(root.left ,level + 1,2 * value);
        boolean right = compute(root.right,level + 1,(2 * value) + 1);
        
        return left && right;
    }
        
    public boolean isCompleteTree(TreeNode root) {
        TreeNode temp = root;
        int level = 0;
        int value = 1;
        while(temp!=null){
            map[level++] = value;
            value*=2;
            temp = temp.left;
        }
        // System.out.println(Arrays.toString(map));
        boolean res =  compute(root,0,1);
        int nodes = 1;
        
        for(int i=2 ; i<=maxLevel ; i++){
            nodes = nodes<<1;
            if(count[i]!=0 && count[i-1]!=nodes){
                return false;
            }
        }
        return res;
    }
}