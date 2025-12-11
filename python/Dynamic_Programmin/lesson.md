

## fib problem : 


When we store a value lets say f(4) which is 5 in the memo map, as if we said every time then we find f(4) (which is five) it is 5 without carrying on the count


fib tree : 

a tree solution means it is from top to down solution : 

![WhatsApp Image 2025-12-10 at 16 25 32_a0c2d749](https://github.com/user-attachments/assets/3086ddf4-6316-4ce3-823a-807fa79f4a35)

Every time we came across an item existing in memo, we replace the path by its value

Until we reach the recursion end point, which is there 0 or one also called base case

In mostly of dp problems, there is a base case where the recurive loop ends


fib solution with brute force : 

![WhatsApp Image 2025-12-11 at 16 48 34_6ca8c91f](https://github.com/user-attachments/assets/359f2da3-7023-4f1b-9cc8-2f5d68fc2c5e)

![WhatsApp Image 2025-12-11 at 16 48 35_284eeaf8](https://github.com/user-attachments/assets/df4a59f0-965c-448b-81eb-7931277896ea)



the normal fib solution without any nested function : 


![WhatsApp Image 2025-12-10 at 18 38 11_d739af54](https://github.com/user-attachments/assets/ee1d9fd4-0496-4161-a673-6ca0931fc79a)


solution with nested func : 

![WhatsApp Image 2025-12-11 at 16 48 35_5a6ff60b](https://github.com/user-attachments/assets/55b52c8e-97eb-43a3-a4c3-0db44c3b3315)


![WhatsApp Image 2025-12-11 at 16 48 35_597c0f9f](https://github.com/user-attachments/assets/c12c87cc-35f1-4e9b-8fbe-c4e2b09552e3)



## coins change : 


We have the coins problem : we have an amount of coins, and we re trying to reach a sum target with minimum and most optimal way

So we gonna start with target sum, and we substract the next node from the parent node

![WhatsApp Image 2025-12-11 at 00 40 44_a41d8d61](https://github.com/user-attachments/assets/dc2da5cd-df97-4ebe-bddc-71bf03ee29ad)


approach : 

![WhatsApp Image 2025-12-11 at 16 33 24_dbd4f1c1](https://github.com/user-attachments/assets/fbe9780c-25d8-4ca2-9b59-542338d4e269)





## notes : 


!!!!!! Every recursion call is a new node !!!!!!


!!!!! If you want a variable that keep updating accross all recursion call, you should declare it in the parent function (recursive function) parameter, to keep updating without overwriting
