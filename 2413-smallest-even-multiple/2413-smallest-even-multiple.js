/**
 * @param {number} n
 * @return {number}
 */
var smallestEvenMultiple = function(n) {
    if ((n&1)==0) return n;
        return 2*n;
};