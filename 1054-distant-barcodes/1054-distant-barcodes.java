class Pair{
    public int key;
    public int value;
    
    public Pair(int key,int value){
        this.key = key;
        this.value = value;
    }
    public String toString(){
        return String.valueOf(this.key)+" : "+String.valueOf(this.value);
    }
}
class SortByValue implements Comparator<Pair>{
    public int compare(Pair a,Pair b){
        return b.value-a.value;
    }
}
class Solution {
    public int[] rearrangeBarcodes(int[] barcodes) {
        HashMap<Integer,Integer> map = new HashMap<>();
        PriorityQueue<Pair> pq =  new PriorityQueue<>(new SortByValue());
        int[] res = new int[barcodes.length];
        
        int value;
        for(int i : barcodes){
            value = map.getOrDefault(i,0);
            map.put(i,value+1);
        }
        for (var entry : map.entrySet()) {
            pq.add(new Pair(entry.getKey(),entry.getValue()));
        }
        // System.out.println(pq);
        int index = 0;
            
        while(pq.size()!=0){
            var obj1 = pq.poll();
            var obj2 = pq.poll();
            if(obj1!=null){
                res[index++] = obj1.key;
                obj1.value-=1;
            }
            if(obj2!=null){
                res[index++] = obj2.key;
                obj2.value-=1;
            }
            if(obj1!=null && obj1.value>=1){
                pq.add(obj1);
            }
            if(obj2!=null && obj2.value>=1){
                pq.add(obj2);
            }
            
        }
        
        return res;
        
        
        
    }
}