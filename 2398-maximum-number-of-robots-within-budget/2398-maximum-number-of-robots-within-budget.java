class Solution {
    public int maximumRobots(int[] chargeTimes, int[] runningCosts, long budget) {
        PriorityQueue<Integer> pq = new PriorityQueue<>(Collections.reverseOrder());
        int prev = 0;
        long sum= 0;
        int res= 0;
        long tempB = 0;
        for(int i = 0 ; i<chargeTimes.length ; i++){
            pq.add(chargeTimes[i]);
            sum+=runningCosts[i];
            tempB = (long)(pq.peek() + (pq.size() * sum));
            while(prev < chargeTimes.length && tempB>budget){
                // System.out.println(tempB+" "+prev+" - "+i);
                sum-=runningCosts[prev];
                pq.remove(chargeTimes[prev++]);
                if(pq.size()==0){
                    tempB=0;
                    break;
                }
                tempB = (long)(pq.peek() + (pq.size() * sum));
            }
            res = Math.max(res,pq.size());
        }
        return res;
    }
}