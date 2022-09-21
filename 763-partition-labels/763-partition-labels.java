class Solution {
    public List<Integer> partitionLabels(String s) {
        List<Integer> res = new ArrayList<>();
        HashMap<Character,Integer> map = new HashMap<>();
        // Stack<Character> stack = new Stack<>();
        
        for(int i = s.length()-1 ; i>-1 ; i--){
            if(!map.containsKey(s.charAt(i))){
                map.put(s.charAt(i) , i);
            }
        }
        // System.out.println(map);
        int pre = 0;
        int index = 0;
        while(index<s.length()){
            char currChar = s.charAt(index);
            int thatIndex = map.get(currChar);
            while(index < thatIndex){
                currChar = s.charAt(index);
                int ii = map.get(currChar);
                if(ii>thatIndex){
                    thatIndex= ii;
                }
                index+=1;
            }
            index = thatIndex+1;
            res.add(index- pre);
            pre = index;
        }
        
        return res;
    }
}