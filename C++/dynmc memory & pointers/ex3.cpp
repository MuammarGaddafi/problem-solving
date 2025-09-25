// Sum of even elements in the array

// Given an array of integers, use a pointer to iterate through it.
// Calculate and print the sum of all even numbers.


#include <iostream> 

int main() {


    int * ptr ; 

    int array[] = {7,7,9,3,8,2,1,777,5,1} ;

    int sum = 0 ;

    ptr = array ;
    

    int length = sizeof(array) / sizeof(array[0]);

    int i=0 ;
    for (i=0 ; i<length ; i++) {

        if ( *(ptr + i ) % 2 == 0 ) {
            std::cout << *(ptr+i) << "\n" ;
            sum=sum+ *(ptr+i) ; 
        }

        
    }

    std::cout << " the sum is " << sum ; 


    return 0 ;

}