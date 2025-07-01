
# what is HASH ?????????? :

a hash is an ID of value that helps us to find things quickly unlike the linear classical access and search, so to hash something is to pass it through a hash function which would return an id (It is about transforming the value into an ID, rather than assigning an ID to it, as many mistakenly believe.

- Hashing: The overall process of converting data into a hash value.
- The number produced from a hash function is called a hash
- So hashmap or hasbtable is map/table of values produced from hash function which are hashs

![WhatsApp Image 2025-06-27 at 15 15 02_81912cf2](https://github.com/user-attachments/assets/f8635ecf-1fe5-454d-9d44-9b863bc31a4a)

Any parameter for hashing should be immutable so we can say it's hashable, because we cannot hash a mutable parameter which can vary at any time, otherwise it cannot be a key, that's why a tuple is hashable because you cannot modify it unlike tables lists sets... Frozen sets by the way could be hashable since they are immutable


![WhatsApp Image 2025-06-27 at 15 19 18_299e9d65](https://github.com/user-attachments/assets/208df27e-575a-4030-949c-8cda40879ca6)

As we see, we take the key of each dictionary as parameter for the hash function, then we get the precised index for it in the table (! The dict key is hashable, not like the whole structure, bcz the dict key is immutable, so we can hash it)

![WhatsApp Image 2025-06-28 at 16 23 51_8f165158](https://github.com/user-attachments/assets/6a79b960-3676-4ef6-a4fe-a0405e8d38cd)

As we see, hashing even give us the opportunity to have a kind of string index, any immutable thing could be an index since the hash function could do the job of transforming it and making it a valid index, like we see on the left array we have normal indexes stock[0] , stock[1] ....
But on the right we can say stock["6 march"] and 6 march there is string which is the key of 340 value in the dictionary, after passing march 6 (which is a date) throug hash function, the return was 0, then we put its corresponding value in stock[0] cell

### hash implementation :
How to implement a hash table also known as hashmap in different programming languages
We notice that in python their implementation is a dictionary


![WhatsApp Image 2025-06-28 at 16 29 40_7d0f3b32](https://github.com/user-attachments/assets/5ce8af7f-75e9-4603-924f-f411a568ef85)


### problems we may face during hashing : 
It's possible that hashing two different keys may result in collision, which is having the same value after hashing them
Methods to avoid and deal with collision : 

Closed adressing : (we use it when the collision is more likely to happen,like we have many values to put which their count would definitely surpass the size of the array by far)

Chaining 

![WhatsApp Image 2025-06-28 at 21 59 14_d95b01bd](https://github.com/user-attachments/assets/dc46fc89-0714-4471-b822-927f54a9b3b4)


Open adressing: (you can put in another cell in the array) 

Linear probing 

![WhatsApp Image 2025-06-28 at 21 59 16_eb1a4ed6](https://github.com/user-attachments/assets/85f80170-5c42-4ae7-90b3-88fcafc7e6de)

Quadratic probing


### use cases : 
Hashing usually used to index and assign huge amounts of data, that's why it is widely used in database indexing, compilers,caching, password authentication etc ..
Example of useful hashing in storing data : 
Let's imagine we have a user who's trying to access his account, he enters his username, so we hash his username to directly get his location in our data base then we now have all the informations needed about his account and we can load them for the user



## conclusion : 
stocking values in normal way :
![WhatsApp Image 2025-06-28 at 21 53 35_a1b493b6](https://github.com/user-attachments/assets/fb57ef11-cdbd-4598-8e04-2af3d0a89f47)
with hashing :
![WhatsApp Image 2025-06-28 at 21 53 35_81765754](https://github.com/user-attachments/assets/1c1a50b1-2919-4d72-9d3c-58b92f01309d)
difference :
![WhatsApp Image 2025-06-28 at 21 53 36_151e3848](https://github.com/user-attachments/assets/573783e0-5578-40c0-a10f-d68027c6efad)

to sum up :
Difference between hash method and normal method to store values and data : 

You a value, lets say integers 1 2 44 5 7 0 99, if you want to store them in classical array they would be stored in indexed cells 0 1 2 3 4 ... 
If you want to search an element then you have to do it linearly 

On the other hand : hashing allow you to access or search any value even if you don't know its index, the hash function would give you the exact index of it 

Example : you need to know where is  "9 march" stored in the array 


-in traditional way : you have to go through the whole array linearly until array[i]=="9 march" 
With hash method :
Hashfunct(9 march) gives you the exact index of it



************************************************************************************************************************************************************


# how to work with hash practically :

One of the most common problem in IT world is managing a large number of data and objects at the same time, as an example, imagine you're building an application that needs to support a large number of user and accounts, that have user name full name display name etc...
New accounts are being added all the time, and older accounts are being deleted also with unused accounts are being deactivated

![WhatsApp Image 2025-06-29 at 14 54 45_eaa3047f](https://github.com/user-attachments/assets/dace0e2e-9772-4167-838d-cbe390f8a0e6)


The simplest way to manage these profiles is to put them all in an array, and there it comes the role of hashing to find the particular account and data to provide the user with the needed services

![WhatsApp Image 2025-06-29 at 14 54 46_229d4170](https://github.com/user-attachments/assets/0eafd444-8278-46fb-bacd-4ecd0f4614af)

but while we work with hashing on problem solving and programming, we do not really need to do this whole process, because most of progrmmin languages offer us a built in hashmaps and free us from doing these steps in most of the times, like in python we do have dictionnariies that take key values, the programm automatically hash these keys and store them in the memory after passing them through hash func also with taking charge of collision managing, the following problems would give you more ideas on how to implement and use the hash map in our favor and to solve complexe problems



