// Copy one array into another using pointers 

// Create a source array with fixed values.
// Dynamically allocate a second array of the same size.
// Use pointers to copy each element from source to destination.
// Print both arrays to verify.

#include <iostream> 

int main() {

    int array[] = {1,6,5,7,8,9,3} ;

    int length = sizeof(array) / sizeof(array[0]);

    int* copy_array= new int [length] ;

    int* ptr=array ; 

    int i ; 

    for (int i = 0; i < length; ++i) {
        copy_array[i] = *ptr;
        ptr = ptr + 1;
    }

    std::cout << "Source: ";
    for (int i = 0; i < length; ++i) {
        std::cout << array[i] << ' ';
    }
    std::cout << '\n';

    std::cout << "Copy:   ";
    for (int i = 0; i < length; ++i) {
        std::cout << copy_array[i] << ' ';
    }
    std::cout << '\n';

    delete[] copy_array;
    return 0;
}