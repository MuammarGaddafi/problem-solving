
## structs : 

When we declare a struct : 

Struct student { } , the student its self becomes kind of a data type

![WhatsApp Image 2026-01-08 at 11 43 04 PM](https://github.com/user-attachments/assets/e0d21346-6fdf-4ac3-bdd7-345a96ac42ef)


Now, lets declare a student variable:

![WhatsApp Image 2026-01-08 at 11 44 26 PM](https://github.com/user-attachments/assets/6257fc4d-8575-44a5-88d9-16db91e0a9a0)

Passing a struct as a parameter to a function in cpp :

![WhatsApp Image 2026-01-08 at 11 47 50 PM](https://github.com/user-attachments/assets/c8d04c27-04e4-4f0b-9b1a-6e7e212e94e9)

!!!! The struct instance name is not a dereference so it is not considered as a pointer like the array name !

If we want to see the adress of car instance, we simply type &car1

When we gonna change a struct instance attribute, we pass it to the function by reference:

![WhatsApp Image 2026-01-08 at 11 52 49 PM](https://github.com/user-attachments/assets/c1cd1b7f-2207-4cac-b4e0-4e1befe3b2d0)



## OOP : 


First of all, the scope resolution :: 

It has 4 main and almost only use cases : 

1 - to access a global variable in certain cases

2 - accessing enum class member :

![WhatsApp Image 2026-01-09 at 11 22 05 AM](https://github.com/user-attachments/assets/08598332-c63f-4543-9442-42f1584e29c4)

3 - accessing name space elements :

![WhatsApp Image 2026-01-09 at 11 22 40 AM](https://github.com/user-attachments/assets/4a815725-beac-4d3b-9bd5-483645fb5a61)

4 - defining a class function outside of the class :

![WhatsApp Image 2026-01-09 at 11 23 09 AM](https://github.com/user-attachments/assets/31529a18-d944-4da1-af8f-da603838dce9)

OOP syntax and explanation :

![WhatsApp Image 2026-01-09 at 11 23 58 AM](https://github.com/user-attachments/assets/2ecf784f-6a6c-4cd8-a3d1-827aa7ffeb57)

So the main core difference that you ‘ ll notice while using OOP in cpp, is the public and private state in class definition, so it may seems absurd and overwhelming at first glance, but dont worry, it is mainly advocating the encapsulation concept like we had in python, as if we said : 

If we want the element (attribute) to be encapsulated and accessed only by setters abd getters, we define it in private state, otherwise we define it in the public one

<img width="1125" height="335" alt="image" src="https://github.com/user-attachments/assets/64bb2382-c339-477c-9a9d-678f81f54839" />

<img width="1125" height="837" alt="image" src="https://github.com/user-attachments/assets/0ab658e2-72ee-4ccf-8436-b346a6623321" />

<img width="1125" height="1028" alt="image" src="https://github.com/user-attachments/assets/d9ed63b4-c365-492c-b0b4-849910add310" />

<img width="1125" height="855" alt="image" src="https://github.com/user-attachments/assets/c92012ed-c1f8-456a-8be1-fc8affe65fc3" />

<img width="1125" height="1102" alt="image" src="https://github.com/user-attachments/assets/6962df85-3c7b-4b6d-8086-f8d32392afca" />

<img width="1125" height="1321" alt="image" src="https://github.com/user-attachments/assets/aa1020e7-a6bf-4ba6-ae7d-0a4e430209ab" />

<img width="1125" height="803" alt="image" src="https://github.com/user-attachments/assets/a92af01b-7d92-4603-9cd5-b69a142145d0" />


## Constructors :

![WhatsApp Image 2026-01-09 at 11 39 58 AM](https://github.com/user-attachments/assets/3791b9b6-f870-4163-b0b1-ea1fa9eec418)

In cpp , the constructor doest the same job as the self initilization method do, but the only difference is we should declare all the attributes that the constructor define above it


And this is like the self alternative so it represents the instance created

!!!!!!!!!!!! The core syntax of oop in cpp !!!!!!!!!!!

![WhatsApp Image 2026-01-09 at 11 44 39 AM](https://github.com/user-attachments/assets/46072875-841a-4918-8da6-e9068e6229b1)

![WhatsApp Image 2026-01-09 at 11 45 58 AM](https://github.com/user-attachments/assets/62f061c1-ea2e-4eab-b03e-ec848185f599)


Overloading in cpp :

![WhatsApp Image 2026-01-09 at 11 50 34 AM](https://github.com/user-attachments/assets/b91dc3e2-cd73-46b0-91e3-f2eb1f87e69d)

In this case, we gonna get error because pizza is not an overloaded function


![WhatsApp Image 2026-01-09 at 11 52 53 AM](https://github.com/user-attachments/assets/6ed5768d-607c-4029-9542-5dfe436805ad)


Simply, we gonna redefine the same function multiple times ( as many overloading cases as we have), and when you construct the object and use the method (even the construction method) it would be automatically matched to the relevant version of the function depending on the parameters entered :

Getters and setters used with Encapsulation :

![WhatsApp Image 2026-01-09 at 11 59 49 AM](https://github.com/user-attachments/assets/ab4c2597-1aea-478d-8eb4-5112e01668e0)

As we have seen, we defined the temperature attribute as a class attribute, so all the objects instanced from this class would have the same temperature value by default, and if we want to change it we use the setters and getters


Inheritance: 

![WhatsApp Image 2026-01-09 at 12 04 21 PM](https://github.com/user-attachments/assets/409895c6-2dc9-429d-9dae-6794c5676701)

![WhatsApp Image 2026-01-09 at 12 05 24 PM](https://github.com/user-attachments/assets/57625539-a739-4f4d-acb2-646e75c506b5)

If we created a dog object, it would have the alive attribute by default, and it would have true as a value

If we want to change the method inherited from the parent class, then it is called over riding the method

!!!!!!!! Inheritance of the parent constructor :

![WhatsApp Image 2026-01-09 at 12 10 56 PM](https://github.com/user-attachments/assets/02394de4-d760-4670-b759-13763a5c12fb)


This is an example of defining children classes, and each one has its own constructor :

![WhatsApp Image 2026-01-09 at 12 11 26 PM](https://github.com/user-attachments/assets/3cc1fe61-bb2f-4e9b-a2fe-7d103fddc772)





