// Dynamic array allocation

// Ask the user for the number of elements.
// Dynamically allocate an array of that size using 'new'.
// Fill it with values, print them, then free the memory using 'delete[]'.

#include <iostream> 

int main()  {

    int the_size ;
    int* array=NULL ;

    std::cout << "give me the size of the array" << "\n" ;
    std::cin >> the_size ; 

    array = new int[the_size] ; 

    int i ;

    for (i=0 ; i<the_size ; i++ ) {
        std::cout << "entrez la valeur de case n° " <<  i+1 << "\n" ;
        std::cin >> array[i] ;


    }

     for (i=0 ; i<the_size ; i++ ) {

        std::cout << array[i] ;
         

    }



    delete[] array ;
    return 0 ;
}