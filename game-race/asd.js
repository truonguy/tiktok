/**
 * @param {integer} init
 * @return { increment: Function, decrement: Function, reset: Function }
 */
var createCounter = function(init) {
    let saveInit = init
    function increment(){
       return init ++;
    }

    function reset() {
        return saveInit
    }

    function decrement() {
        return saveInit --
    }
};

/**
 * const counter = createCounter(5)
 * counter.increment(); // 6
 * counter.reset(); // 5
 * counter.decrement(); // 4
 */