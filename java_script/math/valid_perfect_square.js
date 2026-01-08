/**
 * @param {number} num
 * @return {boolean}
 */
var isPerfectSquare = function(num) {
    
    let left = 1 , right = num 


    let output=false



    while (left <= right) {

        let middle = left + Math.floor((right - left) / 2) 

        if ( middle*middle > num ) {

            right = middle - 1 
        }

        else if ( middle*middle < num ) {

            left = middle + 1 
        }

        else if (middle*middle == num) {

            output = true
            break 
        }

    }

    return output
};