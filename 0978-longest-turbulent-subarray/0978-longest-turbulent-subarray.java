class Solution {
    public int maxTurbulenceSize(int[] arr) {
        // if(arr.length==1)return 1;
        
        int res = 0;
        int c = 0;
        int previous = 10;
        for(int i = 1 ; i < arr.length ; i++){
            if(arr[i]-arr[i-1] > 0     && (previous==-1 || previous==10)){
                c+=1;
                previous=1;
            }    
            else if(arr[i]-arr[i-1] < 0 && (previous==1 || previous==10)){
                c+=1;
                previous=-1;
            }
            else{
                // System.out.println("Interrupt at "+i+" "+arr[i]);
                res = Math.max(res,c);
                if(arr[i]-arr[i-1] > 0){
                    previous=1;
                    c=1;
                    // System.out.println("proceed with "+previous);
                }
                else if(arr[i]-arr[i-1] < 0){
                    previous=-1;
                    c=1;
                    // System.out.println("proceed with "+previous);
                }
                else{
                    previous=10;
                    c=0;
                    // System.out.println("proceed with "+previous);
                }
            }
            res = Math.max(res,c);
        }
        res = Math.max(res,c);
        return res+1;
    }
}