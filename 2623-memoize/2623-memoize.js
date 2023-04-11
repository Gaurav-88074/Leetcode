/**
 * @param {Function} fn
 */
function memoize(fn) {
    var map  = new Map();
    return function(...args) {
        let key = JSON.stringify(args);
        if(map.has(key)){
            return map.get(key);
        }
        else{
            map.set(key,fn(...args));
            return map.get(key);
        }
    }
}


/** 
 * let callCount = 0;
 * const memoizedFn = memoize(function (a, b) {
 *	 callCount += 1;
 *   return a + b;
 * })
 * memoizedFn(2, 3) // 5
 * memoizedFn(2, 3) // 5
 * console.log(callCount) // 1 
 */