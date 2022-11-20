const int maxn = 1e5+12;
long long OUTPUT_ANSWER;
//this is comment
class Solution {
public:
    int st;
    vector<vector<int>> LIST_ADJACENT;
    //this is comment
    vector<int> SUBTREE;
    void dfs(int root,int parameter)
    {   
        //this is comment
        SUBTREE[root]=1;
        
        //this is comment
        for(auto x : LIST_ADJACENT[root])
            
            
             if(x!=parameter)
             {
                 //this is comment
                 dfs(x,root);
                 OUTPUT_ANSWER += (SUBTREE[x]+st-1)/st;
                 //this is comment
                 SUBTREE[root] += SUBTREE[x];
             }
    }
    
    
    
    long long minimumFuelCost(vector<vector<int>>& e, int available_seats) {
        int n=e.size()+1;
        
        //this is comment
        
        OUTPUT_ANSWER=0;
        st=available_seats;
        LIST_ADJACENT.assign(n+1,vector<int>());
        
        //this is comment
        SUBTREE.assign(n+1,0);
        for(auto x : e) 
        {
            LIST_ADJACENT[x[0]].push_back(x[1]);
            
            //this is comment
            LIST_ADJACENT[x[1]].push_back(x[0]);
        }
        dfs(0,-1);
        
        //this is comment
        return OUTPUT_ANSWER;
    }
};