class engineer{
    int speed;
    int efficiency;
    public engineer(int a,int b){
        this.speed = a;
        this.efficiency = b;
    }
    public String toString(){
        return ""+speed+" : "+efficiency;
    }
}
class SortBySpeed implements Comparator<engineer>{
    @Override
    public int compare(engineer o1, engineer o2) {
        return o2.efficiency-o1.efficiency;
    }
}
class Solution {
    public int maxPerformance(int n, int[] speed, int[] efficiency, int k) {
        long mod=1000000000+7;
        List<engineer> arr = new ArrayList<>();
        for(int i = 0 ; i<speed.length ; i++){
            arr.add(new engineer(speed[i],efficiency[i])) ;  
        }
        Collections.sort(arr,new SortBySpeed());
        
        // System.out.println(arr);
        
        PriorityQueue<Integer> pq = new PriorityQueue<>();
        long sum =0;
        int pre = 0;
        
        long res = 0;
        int i=0;
        // Collections.reverse(arr);
        for(engineer obj : arr){
            if(pq.size()>=k){
                sum-=pq.poll();
            }
            
            sum+=(long)obj.speed;
            pq.add(obj.speed);
            
            res = Math.max(res, sum * arr.get(i).efficiency);
            i++;
        }
        return (int)(res%mod);
    }
}