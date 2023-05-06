/**
 * @param {Array} arr
 * @return {Generator}
 */
var inorderTraversal = function(array) {
    let res = []
    function dfs(arr){
        if (Array.isArray(arr)===false){
            res.push(arr);
            return
        }
        for (const index in arr){
            dfs(arr[index])
        }
    }
    dfs(array)
    
    // console.log(res)
    // return res
    let i = 0
    return {
        next : function(){
            let ii = i;
            i+=1;
            if(ii==res.length){
                return {
                    done :  true
                }
            }
            return {
                
                value : res[ii],
                done :  ii==res.length
            }
        }
    }    
};


/**
 * const gen = inorderTraversal([1, [2, 3]]);
 * gen.next().value; // 1
 * gen.next().value; // 2
 * gen.next().value; // 3
 */