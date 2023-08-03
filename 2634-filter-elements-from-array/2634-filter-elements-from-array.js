/**
 * @param {number[]} arr
 * @param {Function} fn
 * @return {number[]}
 */
var filter = function(arr, fn) {
    var sol = []
    for( var i = 0 ; i < arr.length ; i ++){
        if(fn(arr[i],i)){
            sol.push(arr[i])
        }
    }
    return sol
};