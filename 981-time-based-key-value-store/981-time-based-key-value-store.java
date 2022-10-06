class Node{
    
    public String value;
    public int timeStamp;
    
    public Node(String value,int timeStamp){
        this.value = value;
        this.timeStamp = timeStamp;
    }
    public String toString(){
        return String.valueOf(this.value)+" : "+String.valueOf(this.timeStamp);
    }
        
}
class SortByTime implements Comparator<Node>{
    public int compare(Node a,Node b){
        return a.timeStamp - b.timeStamp;
    }
}
class TimeMap {
    public HashMap<String,TreeSet<Node>> map;
    public TimeMap() {
        this.map = new HashMap<>();
    }
    
    public void set(String key, String value, int timestamp) {
        TreeSet<Node> set = map.getOrDefault(key, new TreeSet<>(new SortByTime() ));
        
        set.add(new Node(value,timestamp));
        map.put(key,set);
        
        // System.out.println(map);
    }
    
    public String get(String key, int timestamp) {
        TreeSet<Node> set = map.get(key);
        if(set==null)return "";
        
        Node obj = set.floor(new Node("",timestamp));
        if(obj==null)return "";
        
        return obj.value;
    }
}

/**
 * Your TimeMap object will be instantiated and called as such:
 * TimeMap obj = new TimeMap();
 * obj.set(key,value,timestamp);
 * String param_2 = obj.get(key,timestamp);
 */