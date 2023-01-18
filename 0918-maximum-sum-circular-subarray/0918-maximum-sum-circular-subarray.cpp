class Solution {
public:
    int maxSubarraySumCircular(vector<int>& nums) {
        //calculating max Subarray sum using kadane's Algo (linear array)
        int max1=INT_MIN, sum=0, total=0;
        for(auto x:nums){
            sum+=x;
            max1=max(max1,sum);
            if(sum<0)
                sum=0;
            total+=x; //calculating sum of elements of nums
        }
        
        int max2=0;
        sum=0;
        for(auto x:nums){
            max1=max(max1,total+max2); //updating max when right sum + x + max left sum>max
            total-=x; //right sum
            sum+=x; //left sum  
            max2=max(max2,sum); //maximum left sum
        }
        return max1;
    }
};