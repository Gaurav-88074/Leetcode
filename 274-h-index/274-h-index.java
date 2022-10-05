class Solution {
    public int binarySearch(int[] array,int start,int end,int key){
        
        if(start>end){
            return -1;
        }
        
        int mid = (start+end)/2;
        if(array[mid]==key){
            if(mid-1>-1 && array[mid-1]==key){
                return binarySearch(array,start,mid-1,key);
            }
            else{
                return mid;
            }
        }
        else if(key<array[mid]){
            return binarySearch(array,start,mid-1,key);
        }
        else{
            return binarySearch(array,mid+1, end ,key);
        }
        
    }
    public int hIndex(int[] array) {
        Arrays.sort(array);
        // System.out.println(Arrays.toString(array));

        int lesser  = 0;
        int greater = 0;
        int index;
        
        int res = 0;
        // int value;
        
        int ii=0;
        int n = array.length;
        for(int value : array){
            if(n-ii <= value){
                res+=1;
            }
            ii+=1;
//             index = binarySearch(array,0,array.length-1,i);
//             lesser = index;
//             greater=array.length-index;
            
//             if( lesser==i){
//                 // res = Math.max(res,greater);
//                 res+=1;
//             }
            
            // System.out.println("target : "+i);
            // System.out.println("lesser  values : "+(index));
            // System.out.println("greater values : "+(array.length-index));
        }
        return res;
    }
}