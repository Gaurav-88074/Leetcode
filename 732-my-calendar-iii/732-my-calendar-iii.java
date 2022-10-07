class book{
    int start;
    int end;
    book(int a,int b){
        this.start = a;
        this.end = b;
    }
}
class SortByStart implements Comparator<book>{
    @Override
    public int compare(book o1, book o2) {
        return o1.start - o2.start;
    }
}
class MyCalendarThree {
    int res = 0;
    TreeMap<Integer,Integer> map;
    public MyCalendarThree() {
        this.map  =  new TreeMap<>();
    }
    
    public int book(int start, int end) {
        map.put(start,map.getOrDefault(start,0)+1);
        map.put(end  ,map.getOrDefault(end,0)-1);
        
        int sum = 0;
        int res = 0;
        for(var entry : map.entrySet()){
            sum+=entry.getValue();
            res = Math.max(res,sum);
        }
        
        return res;
    }
}

/**
 * Your MyCalendarThree object will be instantiated and called as such:
 * MyCalendarThree obj = new MyCalendarThree();
 * int param_1 = obj.book(start,end);
 */