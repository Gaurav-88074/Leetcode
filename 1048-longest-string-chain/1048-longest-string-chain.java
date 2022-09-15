class Solution {
    private Integer[][] dp;
    public boolean isSubsequence(String s, String t) {
        int p = 0;
        int size = s.length();
        if(size==0){
            return true;
        }
        for(char c : t.toCharArray()){
            if(c==s.charAt(p)){
                p+=1;
            }
            if(p==size){
                return true;
            }
        }
        return false;
    }
    public boolean isPossible(int index,int curr,String[] words){
        if(curr==-1){
            return true;
        }
        String a = words[index];
        String b = words[curr];
        
        return a.length()-b.length()==1 && isSubsequence(b,a);
    }
    public int compute(String[] words,int index,int curr){
        if(index==words.length){
            return 0;
        }
        
        if(curr!=-1 && dp[index][curr]!=null) return dp[index][curr];
        
        int take = 0;
        int skip = 0;
        
        if(isPossible(index,curr,words)){
            take = 1 + compute(words,index+1,index);
        }
        skip = compute(words,index+1,curr);
        
        int res = Math.max(take,skip);
        
        if(curr!=-1) dp[index][curr] = res;
        return res;
    }
    public int longestStrChain(String[] nums) {
        
        //words-->nums
        
        if(nums.length==1) return 1;
        
        Arrays.sort(nums, (a, b)-> a.length() - b.length());
        
        dp = new Integer[nums.length+1][nums.length+1];
        
        int res = compute(nums,0,-1);
        
        return res;
    }
}