class Solution {
public:
    vector<int> findDuplicates(vector<int>& nums) {
        vector<int> res;
        
        for(auto &x : nums){
            if (nums[abs(x)-1] < 0)
                res.push_back(abs(x));
            else
                nums[abs(x)-1] *= -1;
        }
        return res;
    }
};