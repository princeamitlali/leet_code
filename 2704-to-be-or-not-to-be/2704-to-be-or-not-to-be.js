/**
 * @param {string} val
 * @return {Object}
 */
var expect = function(val) {
    var toBe = (v) =>{
        if (v === val){
            return true 
        } else{
            throw "Not Equal"
        }
    }
    var notToBe = (va) =>{
        // console.log(va,val)
        if (va !== val){
            return true 
        } else{
            throw "Equal"
        }
    }
    
    return {toBe,notToBe}
    
};

/**
 * expect(5).toBe(5); // true
 * expect(5).notToBe(5); // throws "Equal"
 */