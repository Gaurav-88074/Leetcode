class pair{
    public int start;
    public int end;
    public pair(int a,int b){
        this.start = a;
        this.end = b;
    }
    public String toString(){
        return "" + start + " : "+end;
    }
}
class SortbyStart implements Comparator<pair> {
    public int compare(pair a, pair b){
        return a.start - b.start;
    }
}
class SortbyEnd implements Comparator<pair> {
    public int compare(pair a, pair b){
        return a.end - b.end;
    }
}
class MyCalendar {
    private TreeSet<pair> startTime;
    // private TreeSet<pair> endTime;
    public MyCalendar() {
        startTime = new TreeSet<pair>(new SortbyStart());
        // endTime   = new TreeSet<pair>(new SortbyStart());
    }
    
    public boolean book(int start, int end) {
        pair v = startTime.floor(new pair(start,-1));
        pair k = startTime.ceiling(new pair(start,-1));
        // System.out.println(start + " - "+end);
        // System.out.println(v);
        // System.out.println(k);
        boolean check1 = false;
        boolean check2 = false;
        if(v==null || v.end<=start){
            check1 = true;
        }
        if(k==null || k.start>=end){
            check2 = true;
        }
        // System.out.println(startTime);
        // System.out.println(endTime);
        // System.out.println("current status : "+(check1&&check2));
        if(check1 && check2){
            startTime.add(new pair(start,end));
            return true;
        }
        return false;
    }
}











/**
 * Your MyCalendar object will be instantiated and called as such:
 * MyCalendar obj = new MyCalendar();
 * boolean param_1 = obj.book(start,end);
 */