class MyCalendarTwo {
public:
    map<int,int> m;
    MyCalendarTwo() {
        
    }
    
    bool book(int start, int end) {
        int sum=0;
        m[start]++;
        m[end]--;
        for(auto x:m){
            sum+=x.second;
            if(sum>2){
                m[start]--;
                m[end]++;
                return false;
            }
        }
        return true;
    }
};