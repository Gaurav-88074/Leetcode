class Solution {
public:
        vector<int> merge(vector<int> &array1,vector<int> &array2){
            vector<int> res(array1.size()+array2.size());
            int p1 = 0;
            int p2 = 0;
            int index = 0;
            while (p1<array1.size() && p2<array2.size()){
                if(array1[p1]<array2[p2]){
                    res[index++] = array1[p1++];
                }
                else{
                    res[index++] = array2[p2++];
                }

            }
            while (p1<array1.size()){
                res[index++] = array1[p1++];

            }
            while (p2<array2.size()){
                res[index++] = array2[p2++];

            }
            return res;
        }
        vector<int> mergeSort(vector<int> &array,int start,int end){
            if (start==end){
                vector<int> res;
                res.push_back(array[end]);
                return res;
            }

            int mid = (start+end)/2;
            vector<int> left  = mergeSort(array,start,mid);
            vector<int> right = mergeSort(array,mid+1,end);
            return merge(left,right);
        }

        vector<int> sortArray(vector<int>& nums) {
            // quickSort(nums,0,nums.size()-1);
            return mergeSort(nums,0,nums.size()-1);
        }
};