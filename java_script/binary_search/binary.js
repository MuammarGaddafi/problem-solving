/**
 * @param {number[]} nums
 * @param {number} target
 * @return {number}
 */
var search = function(nums, target) {
    

    
let left = 0 , right = nums.length - 1 , middle = ( Math.floor(nums.length / 2 )) 

let output = -1



while ( left <= right ) {



    if ( nums[middle] < target ) {

        left = middle + 1
        middle =  left + (  Math.floor((right - left )/2)   )
    }

    else if ( nums[middle] > target ) {

        right = middle - 1 
        middle =  left + (  Math.floor((right - left )/2)   )

    }

    else if ( nums[middle] === target ) {

        output=middle
        break
        
    }
}


return output
};