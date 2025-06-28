
# what is HASH ?????????? :

a hash is an ID of value that helps us to find things quickly unlike the linear classical access and search, so to hash something is to pass it through a hash function which would return an id (It is about transforming the value into an ID, rather than assigning an ID to it, as many mistakenly believe.

![WhatsApp Image 2025-06-27 at 15 15 02_81912cf2](https://github.com/user-attachments/assets/f8635ecf-1fe5-454d-9d44-9b863bc31a4a)

Any parameter for hashing should be immutable so we can say it's hashable, because we cannot hash a mutable parameter which can vary at any time, otherwise it cannot be a key, that's why a tuple is hashable because you cannot modify it unlike tables lists sets... Frozen sets by the way could be hashable since they are immutable


![WhatsApp Image 2025-06-27 at 15 19 18_299e9d65](https://github.com/user-attachments/assets/208df27e-575a-4030-949c-8cda40879ca6)

As we see, we take the key of each dictionary as parameter for the hash function, then we get the precised index for it in the table (! The dict key is hashable, not like the whole structure, bcz the dict key is immutable, so we can hash it)

### problems we may face during hashing : 
It's possible that hashing two different keys may result in collision, which is having the same value after hashing them
Methods to avoid and deal with collision : 

Closed adressing : (we use it when the collision is more likely to happen,like we have many values to put which their count would definitely surpass the size of the array by far)

Chaining 

Open adressing: (you can put in another cell in the array) 

Linear probing 
Quadratic probing


### use cases : 
Hashing usually used to index and assign huge amounts of data, that's why it is widely used in database indexing, compilers,caching, password authentication etc ..
