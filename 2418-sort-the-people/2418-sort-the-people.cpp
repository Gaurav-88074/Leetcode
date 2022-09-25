class person{
    public:
        int h;
        string name;
        
        person(string &n,int &h){
            this->h = h;
            this->name = n;
        }
};
class Solution {
public:
    vector<string> sortPeople(vector<string>& names, vector<int>& heights) {
        vector<person> temp;
        for(int i =0; i<names.size() ; i++){
            temp.push_back(person(names[i],heights[i]));
        }
        sort(temp.begin(),temp.end(),[](person &a,person &b){
            return b.h<a.h;
        });
        vector<string> res;
        for(person &obj : temp){
            res.push_back(obj.name);
        }
        return res;
        
    }
};
