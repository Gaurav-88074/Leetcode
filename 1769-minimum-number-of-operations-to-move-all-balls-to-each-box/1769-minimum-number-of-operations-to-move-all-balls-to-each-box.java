class Solution {
    public int[] minOperations(String boxes) {
        int[] left  = new int[boxes.length()];
        int[] right = new int[boxes.length()];
        int[] res   = new int[boxes.length()];
        
        List<Integer> stack = new LinkedList<>();
        
        int value = 0;
        int ans = 0;
        
        for(int i=0 ; i<boxes.length() ; i++){
            value = boxes.charAt(i)-48;
            
            ans = 0;
            for(int v : stack){
                ans+=(i-v);
            }
            left[i] = ans;
            
            if(value==1){
                stack.add(i);
            }
        }
        stack.clear();
        
        for(int i=boxes.length()-1 ; i>=0 ; --i){
            value = boxes.charAt(i)-48;
            
            ans = 0;
            for(int v : stack){
                ans+=(v-i);
            }
            right[i] = ans;
            
            if(value==1){
                stack.add(i);
            }
        }
        // System.out.println(Arrays.toString(left));
        // System.out.println(Arrays.toString(right));
        
        for(int i = 1; i < boxes.length()-1 ; i++){
            res[i] = left[i] + right[i];
        }
        res[0] = right[0];
        res[boxes.length()-1] = left[boxes.length()-1];
        
        return res;
        
    }
}