

### defining a string as const char or std::string : 

std::string is the common way of declaring a string just like in python, it is a string object, in the other hand const char is like declaring an array of char that consists a string, so it is mainly similar to all array characteristics : immutable, its name is a pointer etc... 


<img width="999" height="372" alt="image" src="https://github.com/user-attachments/assets/bd1382dc-eba8-415e-9775-d59866b796e8" />



even when it comes to pointers, const char behaves identically to an array, its pointer is its name, and points to the first element while the std char object pointer pointd to the whole string as one object


### declaring data structure with mixed and different types of values (mainly a vector) : 

![WhatsApp Image 2025-09-28 at 17 57 09_6a3953e4](https://github.com/user-attachments/assets/22f4ebcd-7482-4ac3-b7d2-80fcb08817ec)



### iterators : 


<img width="994" height="870" alt="image" src="https://github.com/user-attachments/assets/9bb2d741-a728-452c-a423-a74f7c2a6b6d" />



### inline functions, lambda alikes in cpp, passing a function as a variable in data structure : 


one of the main utilities of lambda functions in C++ is exactly that: to create inline, unnamed functions without needing a separate declaration.

Suntax : 

[capture](parameters) -> return_type { body }


Example : 


auto add = [](int x, int y) { return x + y; };

std::cout << add(3, 5);  // Output: 8

![WhatsApp Image 2025-11-03 at 17 35 34_d55373c1](https://github.com/user-attachments/assets/804a3be1-d970-42b2-8c35-4484c80a2e33)


example (by the way we could have used defined functions and put their names as the unordered list values) : 


<img width="620" height="213" alt="image" src="https://github.com/user-attachments/assets/f9185eb8-f90f-4ced-a278-beccffa6c57d" />


and this is how we use them : 

<img width="278" height="29" alt="image" src="https://github.com/user-attachments/assets/8bd0196b-7e64-4a33-a73d-c326d66400bc" />



