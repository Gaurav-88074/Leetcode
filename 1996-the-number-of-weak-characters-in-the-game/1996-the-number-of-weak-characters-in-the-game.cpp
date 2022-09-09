class Solution {
public:
    // We are checking that for each element , there exist a Next greater elemenet
    
    //(Increased defence value is existing or not)
    
    // If existing then include in our answer
    
    static bool compare(vector<int> &a , vector<int> &b)
    {
        if(a[0]==b[0])
        {
            return a[1]>b[1];
        }
        
        return a[0]<b[0];
    }
    int numberOfWeakCharacters(vector<vector<int>>& nums) {
        
        int n=nums.size();
        
        // See this is a greedy question 
        
        // sorted in terms of starting value , & if starting value is same
        
        // then we will put the max_end value first
        
        sort(nums.begin() , nums.end() , compare);
     
        vector<int> nge(n , n); // Find next greater element of the curr_val (defence as attack is already sorted )
        
        stack<int> stk;
        
        for(int i=nums.size()-1;i>=0;i--)
        {
            while(!stk.empty() && (nums[stk.top()][1]<=nums[i][1]))
            {
                stk.pop();
            }
            
            if(!stk.empty())
            {
                nge[i]=stk.top();
            }
            
            stk.push(i);
        }
        
        int ans=0;
        
        for(int i=0;i<nums.size();i++)
        {
            if(nge[i]!=n)
            {
                ans++;
            }
        }
        
        return ans;
    }
};