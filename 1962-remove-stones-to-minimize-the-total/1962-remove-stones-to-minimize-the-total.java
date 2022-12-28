class SortByThis implements Comparator<Integer>{
    @Override
    public int compare(Integer o1, Integer o2) {
        // TODO Auto-generated method stub
        int v1 = o1/2;
        int v2 = o2/2;
        if(v1==v2){
            return o1-o2;
        }
        return v1>v2 ? -1 : 1;
    }
    
}
class Solution {
    public int minStoneSum(int[] piles, int k) {
        SortByThis comp = new SortByThis();

        PriorityQueue<Integer> pq = new PriorityQueue<>(comp);
        for(int i : piles){
            pq.add(i);
        }
        int res = 0;
        int value;
        // System.out.println(pq);
        for(int i= 0 ; i<k ; i++){
            value = pq.poll();
            // System.out.println(value);
            value = value - (value/2);
            pq.add(value);
        }
        while(pq.size()!=0){
            res+=pq.poll();
        }
        return res;
    }
}