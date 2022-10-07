class MyCalendarTwo {
    
    TreeMap<Integer,Integer> map;
    public MyCalendarTwo() {
        this.map = new TreeMap<>();
    }
    
    public boolean book(int start, int end) {
        map.put(start,map.getOrDefault(start,0) + 1);
        map.put(end  ,map.getOrDefault(end  ,0) - 1);
        
        int sum = 0;
        for(var entry : map.entrySet()){
            sum+=entry.getValue();
            if(sum>2){
                map.put(start,map.getOrDefault(start,0) - 1);
                map.put(end  ,map.getOrDefault(end  ,0) + 1);
                return false;
            }
        }
        return true;
    }
}

/**
 * Your MyCalendarTwo object will be instantiated and called as such:
 * MyCalendarTwo obj = new MyCalendarTwo();
 * boolean param_1 = obj.book(start,end);
 */