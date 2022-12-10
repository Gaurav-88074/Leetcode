class Solution {
public:
    int maxStarSum(vector<int>& vals, vector<vector<int>>& edges, int k) {
        
        int n = vals.size(),ans = INT_MIN;
        
        vector<vector<int>> sums(n);
        
        for(int i=0; i<edges.size(); i++)
        {
            if(vals[edges[i][1]] > 0) sums[edges[i][0]].push_back(vals[edges[i][1]]);
            if(vals[edges[i][0]] > 0) sums[edges[i][1]].push_back(vals[edges[i][0]]);
        }
        
        for(int i = 0; i<n; i++)
        {
            sort(sums[i].rbegin(), sums[i].rend());
            
            int t = vals[i];
            for(int j = 0; j < min(k, (int)sums[i].size()); j++) t += sums[i][j];
            ans = max(ans,t);
        }
        
        return ans;
    }
};