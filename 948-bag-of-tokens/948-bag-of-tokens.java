class Solution {
    public int bagOfTokensScore(int[] tokens, int power) {
        if(tokens.length==0)return 0;
        
        Arrays.sort(tokens);
        
        int left = 0;
        int right=tokens.length-1;
        int ans=0;
        int res = 0;
        while(left<right){
            if(tokens[left]<=power){
                power-=tokens[left];
                left+=1;
                res+=1;
                ans = res<ans ? ans : res;
            }
            else if(res>0){
                power+=tokens[right];
                res-=1;
                right-=1;
            }
            else{
                break;
            }
            
        }
        if(tokens[left]<=power){
            power-=tokens[left];
            left+=1;
            res+=1;
            ans = res<ans ? ans : res;
        }
        // System.out.println(Arrays.toString(tokens));
        return ans;
    }
}