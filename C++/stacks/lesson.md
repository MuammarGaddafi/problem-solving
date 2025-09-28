<h1>STACKS IN C++</h1>


In cpp, the stack elements are not indexed so you can only access the top element,  by top function, unlike stacks in python which actually are normal lists not real stacks such as cpp


## Creating a stack in cpp :


![WhatsApp Image 2025-09-27 at 16 03 05_9ff48819](https://github.com/user-attachments/assets/74ac5e1a-4e32-42e4-9544-541b1e34eef9)


## stacks functions    : 


* Empty : verifies if the stack is empty : 

![WhatsApp Image 2025-09-27 at 16 04 50_b434fe8d](https://github.com/user-attachments/assets/b9dd9d96-910e-49cb-9742-6264e355ecb8)


* Size : return the size of the stack :

![WhatsApp Image 2025-09-27 at 16 06 30_1eafd160](https://github.com/user-attachments/assets/3103367f-8596-4866-bf68-9134dbee723f)


* Push : add an element on the top of the stack :

![WhatsApp Image 2025-09-27 at 16 10 47_f92999b9](https://github.com/user-attachments/assets/b5580b99-4eea-4250-b92d-bebc37f45d5b)


* Pop : removes the first element of the stack, which is on the top, unlike python, pop doesn't return the popped element, it is a procedure that only pops the stack and doesn't return anything


![WhatsApp Image 2025-09-27 at 16 13 35_566ee63d](https://github.com/user-attachments/assets/41299053-3337-4a81-bb19-83257a62c327)


* Top : access to the top element of the stack



We can make a function that loops over the stacks element without modifying the original stack, by passing the original stack by value to this function (so it would take a copy not modifying the real one) and we will loop over it and do the wanted process, like we did in this example :


![WhatsApp Image 2025-09-27 at 16 20 12_044bed0c](https://github.com/user-attachments/assets/58efbf07-1d9c-41ec-b747-0009711a4c00)


