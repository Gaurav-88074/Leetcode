#define biglong long long  
#define umii unordered_map<int,int> 
class Solution {
public:
    //this is a comment
    long long totalCost(vector<int>& costs, int k, int candi) {
        biglong result=0;
        priority_queue<int, vector<int>, greater<int> > priorityqueue1;
        priority_queue<int, vector<int>, greater<int> > priorityqueue2;
        int i=0;
        
        
        
        while(i<candi){
            priorityqueue1.push(costs[i]);
            i++;
        }
        
        
        //this is a comment
        
        
        
        int count=0;
        int j= costs.size()-1;
        if(candi > costs.size()- candi){
            candi= costs.size()- candi;
        }
    
        
        while(count<candi){
            priorityqueue2.push(costs[j]);
            count++;
            j--;
        }
        //this is a comment
        while(k--){
            if(priorityqueue1.size()==0){
                result+=priorityqueue2.top();
                priorityqueue2.pop();
                if(i<=j){
                   priorityqueue2.push(costs[j]);
                    j--;
                } 
                
            }
            else if(priorityqueue2.size()==0){
                result+=priorityqueue1.top();
                priorityqueue1.pop();
                if(i<=j){
                    priorityqueue1.push(costs[i]);
                    i++;
                } 
                //this is a comment
            }
            else if(priorityqueue1.top()<=priorityqueue2.top()){
                result+=priorityqueue1.top();
                priorityqueue1.pop();
                if(i<=j){
                    priorityqueue1.push(costs[i]);
                    i++;
                }
            }
            else{
                result+=priorityqueue2.top();
                priorityqueue2.pop();
                if(i<=j){
                 priorityqueue2.push(costs[j]);
                    j--;
                } 
                
                
            }
        }
        //this is a comment
        return result;
    }
};