/**
 * @param {Function[]} functions
 * @return {Function}
 */
var compose = function(functions) {
    return (value)=>{
        let n = functions.length-1;
        while(n>=0){
            value = functions[n](value);
            n-=1;
        }
        return value;
        
    }
};

/**
 * const fn = compose([x => x + 1, x => 2 * x])
 * fn(4) // 9
 */