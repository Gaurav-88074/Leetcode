class BrowserHistory {
    public List<String> history ;
    public int size = 0;
    public int i = -1;
    public BrowserHistory(String homepage) {
        history = new ArrayList<>();
        history.add(homepage);
        i++;
        size++;
    }
    
    public void visit(String url) {
        if(i+1 == history.size()){
            history.add(url);
            i++;
            size++;
        }
        else{
            history.set(i+1,url);
            i = i + 1;
            size = i + 1;
        }
    }
    
    public String back(int steps) {
        i = i - steps;
        i = Math.max(0,i);
        if(i>=size){
            return null;
        }
        return history.get(i);
    }
    
    public String forward(int steps) {
        i = i + steps;
        i = Math.min(i , size - 1);
        //----------------
        i = Math.max(0,i);
        //----------------
        if(i>=size){
            return null;
        }
        // System.out.println(history+" "+i+" size "+size);
        return history.get(i);
        
    }
}

/**
 * Your BrowserHistory object will be instantiated and called as such:
 * BrowserHistory obj = new BrowserHistory(homepage);
 * obj.visit(url);
 * String param_2 = obj.back(steps);
 * String param_3 = obj.forward(steps);
 */