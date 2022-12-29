import java.util.Comparator;
import java.util.PriorityQueue;

class Task{
    public int enqueTime;
    public int processingTime;
    public int index;

    public Task(int index,int a,int b){
        this.index = index;
        this.enqueTime = a;
        this.processingTime = b;
    }
    public String toString(){
        return ""+this.index+" "+this.enqueTime+" "+this.processingTime;
    }
}
class SortByThis implements Comparator<Task>{
    
    @Override
    public int compare(Task o1, Task o2) {
        // if( o1.processingTime==o2.processingTime
        //         &&
        //     o1.enqueTime == o2.enqueTime){
        //     return o1.index - o2.index; 
        // }
        if(o1.processingTime==o2.processingTime){
            return o1.index-o2.index;
        }
        return o1.processingTime - o2.processingTime;
    }  
}
class TaskComp implements Comparator<Task>{
    
    @Override
    public int compare(Task o1, Task o2) {
        // if( o1.processingTime==o2.processingTime
        //         &&
        //     o1.enqueTime == o2.enqueTime){
        //     return o1.index - o2.index; 
        // }
        if(o1.enqueTime==o2.enqueTime){
            return o1.processingTime - o2.processingTime;
        }
        return o1.enqueTime - o2.enqueTime;
    }  
}
class Solution {
    public int[] getOrder(int[][] tasks) { 
        // Arrays.sort(tasks,(a,b)->(a[0]-b[0]==0 ? a[1]-b[1] : a[0]-b[0]));
        // System.out.println(Arrays.toString(tasks));
         
        PriorityQueue<Task> pq = new PriorityQueue<>(new SortByThis());
        List<Task> l = new ArrayList<>();  

        int[] res = new int[tasks.length]; 
         
        int ri =0;   
        int i = 0;
        
        for(int[] task : tasks){
            l.add(new Task(i,task[0],task[1]));
            i+=1;
        }
        Collections.sort(l,new TaskComp());
        // System.out.println(l); 
         
        pq.add(l.get(0));
        i = 1;
        int till = pq.peek().enqueTime;
        while(pq.size()!=0){
            Task obj = pq.poll(); 
            
            res[ri++] = obj.index;
            
            till = Math.max(
                till + obj.processingTime ,
                obj.enqueTime + obj.processingTime 
            );
            
            while(i<l.size() && l.get(i).enqueTime<=till){
                pq.add(l.get(i));
                i+=1;
            }
            if(pq.size()==0 && i<l.size()){
                pq.add(l.get(i));
                i+=1;
            }
        }
        // System.out.println(Arrays.toString(res));
        // return new int[]{0,2,3,1};
        return res;
    }
}