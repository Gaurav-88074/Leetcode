class Solution {
public:
    long long dp[100005][3][4];
    long long helper(int idx,string &str,char prev,int len){
        
        if(len==3){
            return 1;
        }
        if(idx>=str.length()){
            return 0;
        }
        
        if(dp[idx][prev-'0'][len]!=-1){
            return dp[idx][prev-'0'][len];
        }
        long long not_take=0;
        long long take=0;
        if(prev!=str[idx]){
            take=helper(idx+1,str,str[idx],len+1);
        }
    
        not_take=helper(idx+1,str,prev,len);
        long long ans=take+not_take;
        dp[idx][prev-'0'][len]=ans;
        return ans;
    }
    long long numberOfWays(string s) {
        memset(dp,-1,sizeof(dp));
        return helper(0,s,'2',0);
    }
};