class Solution {
    public int distinctPrimeFactors(int[] array) {
       HashSet<Integer> h = new HashSet<Integer>();

        for(int i=0; i<array.length; i++){
            int squareroot =(int) Math.sqrt(array[i]);

            for(int j=2; j<=squareroot; j++){
                if(array[i]%j==0){
                    h.add(j);

                    while(array[i]%j==0){
                        array[i] /= j;
                    }
                }
            }
            if(array[i]>1){
                h.add(array[i]);
            }
        }
        return h.size();
    }
}