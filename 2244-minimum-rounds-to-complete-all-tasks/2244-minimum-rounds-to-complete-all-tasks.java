class node{
    public int num;
    public int count;
    public node(int a,int b){
        this.num=a;
        this.count=b;
    }
    public String toString(){
        return ""+this.num+" "+this.count;
    }
}
class SortByThis implements Comparator<node>{

    @Override
    public int compare(node o1, node o2) {
        // TODO Auto-generated method stub
        return -(o1.count-o2.count);
    }  
}
class Solution {
    public int minimumRounds(int[] tasks) {
        PriorityQueue<node> pq = new PriorityQueue<>(new  SortByThis());
        HashMap<Integer,Integer> d = new HashMap<>();
        for(int i : tasks){
            d.put(i , d.getOrDefault(i,0)+1);
        }
        // System.out.println(d);
        for(Map.Entry<Integer,Integer> entry  : d.entrySet()){
            pq.add(new node(entry.getKey(),entry.getValue()));
        }
        // System.out.println(pq);
        int res = 0;
        while (pq.size()!=0){
            node obj = pq.poll();
            // System.out.println(obj);
            
            if(obj.count>=3 && obj.count-3!=1){
                obj.count-=3;
                
                if(obj.count!=0)
                pq.add(obj);
            } 
            else if(obj.count>=2){
                obj.count-=2;
                if(obj.count!=0)
                pq.add(obj);
                
                // res+=1;
                // continue; 
            }
            else{ 
                return -1;
            }
            res+=1;
        }
        return res;
    }
}