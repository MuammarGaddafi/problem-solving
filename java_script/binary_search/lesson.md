Binary search is to search for an element in a sorted array by chopping the search area into a half until we find the element

![WhatsApp Image 2025-12-11 at 17 23 58_bd94897a](https://github.com/user-attachments/assets/920853ac-3a5f-43de-ab0b-d77dd626ccfb)


![WhatsApp Image 2025-12-11 at 18 09 34_d35f1f85](https://github.com/user-attachments/assets/3d09da04-100f-4831-9a75-165fc7320103)


Binry search approach : 

We define the variables :

If the middle is not the target, we check whether it is bigger or smaller thant the target, if it is smaller, we update our left to be midd point + 1 , the right one remains intact, and the middle one gonne update to be the middle of the newer block :

![WhatsApp Image 2025-12-11 at 18 20 02_e0ae26cd](https://github.com/user-attachments/assets/f5d3fae9-a66d-4b79-aaa3-b8b00bb3ffbd)

![WhatsApp Image 2025-12-11 at 18 20 39_eede82db](https://github.com/user-attachments/assets/2b7a15cc-04f0-4603-9277-bf38957ac295)

The last step where mid point and target meet up :

![WhatsApp Image 2025-12-11 at 18 21 45_6ac389c5](https://github.com/user-attachments/assets/e0d8e3db-9522-4284-98b4-63de1558c7e1)



## implementation (cpp) : 

<img width="1638" height="698" alt="image" src="https://github.com/user-attachments/assets/e174578e-0bfb-4d54-be8d-2f5b2fc7d648" />
