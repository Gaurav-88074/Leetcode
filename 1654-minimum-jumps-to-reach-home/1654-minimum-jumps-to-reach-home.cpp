class Solution {
public:
unordered_map<int,int>mp;
int dp[6001][2];
int fun(int i, int c,int a, int b, int x)
{
if(i==x)return 0;
if(i<0 or i>6000 or c>=2 or mp.find(i)!=mp.end())return 1e9;

    if(dp[i][c]!=-1)return dp[i][c];
    
    dp[i][c]=1+fun(i+a,0,a,b,x);
    if(!c)
        dp[i][c]=min(dp[i][c],1+fun(i-b,c+1,a,b,x));
    
    return dp[i][c];
}
int minimumJumps(vector<int>& forbidden, int a, int b, int x) {
    for(int i=0;i<forbidden.size();i++)
        mp[forbidden[i]]=1;
    memset(dp,-1,sizeof(dp));
    
    int res=fun(0,0,a,b,x);
    if(res>=1e9)return -1;
    return res;
}
};