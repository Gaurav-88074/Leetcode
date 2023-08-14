class job{
    public :
        int start;
        int finish;
        int profit;

        job(int start,int finish,int profit){
            this->start = start;
            this->finish=finish;
            this->profit=profit;
        }
};
class Solution {
public:
    int binarySearch(vector<job> &jobs,int index){
        int low = 0;
        int high = index-1;
        int mid;
        while(low<=high){
            mid = (low+high)/2;
            if(jobs[mid].finish<=jobs[index].start){
                if (jobs[mid+1].finish<=jobs[index].start){
                    low = mid+1;
                }
                else{
                    return mid;
                } 
            }
            else{
                high = mid-1;
            }
        }
        return -1;
    }
    int schedule(vector<job> &jobs){
        int total[jobs.size()];
        total[0] = jobs[0].profit;
        int l,p;
        for (int i = 1; i < jobs.size(); i++){
            l = binarySearch(jobs,i);
            p=jobs[i].profit;
            if (l!=-1){
                p+= total[l];
            }
            total[i] = max(p,total[i-1]);
        }
        int res = total[0];
        for(auto e : total){
            res =max(e,res);
        }
        return res;
        // return total[jobs.size()-1];
    }

    int jobScheduling(vector<int>& startTime, vector<int>& endTime, vector<int>& profit) {
        vector<job> jobs;

        for(int i=0 ;i<startTime.size();i++){
           jobs.push_back(job(startTime[i],endTime[i],profit[i]));
        }
        sort(jobs.begin(),jobs.end(),[](job a,job b){
            return a.finish<b.finish;
        });
        //90
        int res = schedule(jobs);
        return res;
    }
};
