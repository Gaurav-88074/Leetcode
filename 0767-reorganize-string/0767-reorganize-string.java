class node{
    public char chr;
    public int count;
    public node(char a,int b){
        this.chr=a;
        this.count=b;
    }
    public String toString(){
        return ""+this.chr+" "+this.count;
    }
}
class SortByThis implements Comparator<node>{

    @Override
    public int compare(node o1, node o2) {
        // TODO Auto-generated method stub
        return -(o1.count-o2.count);
    }  
}
class Solution {
    public String reorganizeString(String s) {
        PriorityQueue<node> pq = new PriorityQueue<>(new  SortByThis());
        int[] d = new int[128];
        for(char c : s.toCharArray()){
            d[c]+=1;
        }
        for(int i = 0 ; i<128 ;i++){
            if(d[i]!=0){
                pq.add(new node((char)i,d[i]));
            }
        }
        // System.out.println(pq);
        StringBuilder sb = new StringBuilder();
        while (pq.size()!=0){
            node obj = pq.poll();
            
            if(sb.length()!=0 && sb.charAt(sb.length()-1)==obj.chr){
                if(pq.size()==0){
                    return "";
                }
                node obj2 = pq.poll();
                sb.append(obj2.chr);
                obj2.count-=1;
                if(obj2.count>0){
                    pq.add(obj2);
                }
                pq.add(obj);
                continue;
            }
            sb.append(obj.chr);
            obj.count-=1;
            if(obj.count>0){
                pq.add(obj);
            }
        }
        return sb.toString();
    }
}