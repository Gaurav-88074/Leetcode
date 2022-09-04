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
    //---------------------------------------------------------------
    private Map< Integer,Map<Integer,ArrayList<Integer>> > map = new TreeMap<>();
    //---------------------------------------------------------------
    public void compute(TreeNode root,int index,int level){
        if(root==null){
            return;
        }
        
        if(map.containsKey(index)){
            Map<Integer,ArrayList<Integer>> innerMap = map.get(index);
            List<Integer> l = innerMap.get(level);
            if(l==null){
                innerMap.put(level,new ArrayList<>(Arrays.asList(new Integer[]{root.val})));
            }
            else{
                l.add(root.val);
            }
        }
        else{
            Map<Integer,ArrayList<Integer>> innerMap = new TreeMap<>();
            innerMap.put(level,new ArrayList<>(Arrays.asList(new Integer[]{root.val})));
            map.put(index,innerMap);
        }
        compute(root.left ,index-1,level + 1);
        compute(root.right,index+1,level + 1);
        
    }
    public List<List<Integer>> verticalTraversal(TreeNode root) {
        int level = 0;
        compute(root,0,0);
        // System.out.println(map);
        List<List<Integer>> res= new ArrayList<>();
        for (Map.Entry< Integer,Map<Integer,ArrayList<Integer>> > entry : map.entrySet()) {
            List<Integer> temp = new LinkedList<>();
            for(Map.Entry< Integer,ArrayList<Integer> > innerEntry : entry.getValue().entrySet() ){
                List<Integer> l = innerEntry.getValue();
                Collections.sort(l);
                // System.out.println(innerEntry.getValue());
                temp.addAll(l);
            }
            res.add(temp);
            // System.out.println(entry.getValue());
            
        }
        return res;
    }
}