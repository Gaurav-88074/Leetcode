class Solution {
    public int evalRPN(String[] tokens) {
        Stack<Integer> stack  = new Stack<>();
        int c;
        int res = 0;
        int a;
        int b;
        int value;
        for(String s : tokens){
            c =  s.charAt(0);
            if( s.length() ==1  
                &&
                (
                    s.charAt(0) =='+' ||
                    s.charAt(0) =='-' ||
                    s.charAt(0) =='/' ||
                    s.charAt(0) =='*'
                ) 
                ){
               
                if(c==43){
                    a = stack.pop();
                    b = stack.pop();
                    res = a+b;
                    stack.add(res);
                }
                else if(c==45){
                    a = stack.pop();
                    b = stack.pop();
                    res = b-a;
                    stack.add(res);
                }
                else if(c==47){
                    a = stack.pop();
                    b = stack.pop();
                    res = b/a;
                    stack.add(res);
                }
                else{
                    a = stack.pop();
                    b = stack.pop();
                    res = a*b;
                    stack.add(res);
                }
            }
            else{
                 stack.add(Integer.parseInt(s));
            }
            // System.out.println(stack);
        }
        return stack.pop();
    }
}