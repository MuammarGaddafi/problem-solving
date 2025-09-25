// Find the maximum element using pointer


#include <iostream> 

int main () {

    int array[] = {1,2,8,9,7,222,9,788,72,85587,897,965,8952,7};

    int* ptr=array ; 

    int length = (sizeof(array)/sizeof(array[0])) ;

    int i ; 

    int max= *ptr ; // first element of the array
    

    for (i = 0; i < length; i++) {
        if (*ptr > max) {
            max = *ptr;
        }

        ptr = ptr + 1;
    }

    std::cout << "this is the maximum of the array : " << max ; 

    return 0 ; 
}