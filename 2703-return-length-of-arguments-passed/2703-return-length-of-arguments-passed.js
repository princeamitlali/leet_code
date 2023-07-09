/**
 * @return {number}
 */
var argumentsLength = function(...args) {
    let text = 0;
    for (let x in args) {
      text += 1
    }
 return text
};

/**
 * argumentsLength(1, 2, 3); // 3
 */