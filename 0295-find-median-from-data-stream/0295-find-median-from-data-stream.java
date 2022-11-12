class MedianFinder {
    private PriorityQueue<Integer> q1 = new PriorityQueue<>(
        Collections.reverseOrder()
    );
    private PriorityQueue<Integer> q2 = new PriorityQueue<>();
    
    public MedianFinder() {
        
    }
    // 1 2 3 4 5 6 8
    // 5 4 3 1 2 6 8
    //maxHeap 2 
    //minHeap 1
    public void addNum(int num) {
        q1.add(num);
        if(q1.size() > q2.size()){
               q2.add(q1.poll());
        }
        else if(q1.size()==q2.size() && q1.peek()>q2.peek()){
            q2.add(q1.poll());
            q1.add(q2.poll());
        }
        // System.out.println(q1);
        // System.out.println(q2);
    }
    
    public double findMedian() {
        
        if(q1.size()<q2.size()){
            return (double)q2.peek();
        }
        else{
            double s = (double)(q1.peek()+q2.peek());
            // System.out.println("s= "+s);
            return (s/2);
        }
    }
}

/**
 * Your MedianFinder object will be instantiated and called as such:
 * MedianFinder obj = new MedianFinder();
 * obj.addNum(num);
 * double param_2 = obj.findMedian();
 */