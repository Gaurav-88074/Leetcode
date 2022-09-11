class Pair{
    int start;
    int end;
    public Pair(int a,int b){
        this.start = a;
        this.end = b;
    }
    public String toString(){
        return ""+start+" : "+end;
    }
}
class SortByStart implements Comparator<Pair>{


    @Override
    public int compare(Pair o1, Pair o2) {
        // TODO Auto-generated method stub
        if(o1.start==o2.start){
            return o1.end-o2.end;
        }
        return o1.start - o2.start;
    }
}
class Solution {
    
    public int minGroups(int[][] intervals) {
        TreeSet<Pair> set = new TreeSet<>(new SortByStart());
        // TreeSet<Pair> set2 = new TreeSet<>(new SortByStart());
        int ex = 0;
        for(int[] i : intervals){
            boolean v = set.add(new Pair(i[0],i[1]));
            if(v==false){
                // set2.add(new Pair(i[0],i[1]));
                ex+=1;
            }
        }
        // System.out.println(set2);
        
        int res = 0;
        while(set.size()!=0){
            res+=1;
            // System.out.println("========");
            Pair obj = set.pollFirst();
            // System.out.println(obj);
            
            Pair temp = new Pair(obj.end+1,0);
            
            Pair next = set.ceiling(temp);
            // System.out.println(next);
            while(next!=null){
                set.remove(next);
                temp = new Pair(next.end+1,0);
                next = set.ceiling(temp);
                // System.out.println(next);
            }
            // System.out.println("========");
        }
        return res+ex;
    }
}