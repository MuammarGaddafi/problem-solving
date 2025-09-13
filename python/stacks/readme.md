# lets see how stacks behave and implemented in python : 



The stack is a simple concept : it is based on storing data in accumulative way, you can only directly access the top value which is the last stored value, if you want to access a specefic value in the stack you should remove all the values on top of it until you reach it

the stack is a linear data structure that follows the Last In First Out principle


this is a filled stack  :


![WhatsApp Image 2025-08-21 at 13 49 48_154f9895](https://github.com/user-attachments/assets/92d34ab5-4bc0-40ee-82b5-148ed4fbc979)


and this is a popped stack :

![WhatsApp Image 2025-08-21 at 13 49 51_e4e52ae2](https://github.com/user-attachments/assets/afd22a28-e616-419f-9a4e-7293351800a5)


Stack functions : (in general) 

![WhatsApp Image 2025-08-21 at 14 17 43_0fb3485e](https://github.com/user-attachments/assets/5e941de5-78a9-4f0f-b286-c5a4d27b8ec2)


This is an example of how a stack class is implemented in python (it is just an example not necessarily stacks are defined like that in python)

![WhatsApp Image 2025-08-21 at 14 19 30_6f4a3e3a](https://github.com/user-attachments/assets/7cb91cf5-1092-4ebc-9ec5-12bb27c95840)

From this example, we can figure out that stacks in python (and maybe in other languages) are mainly lists that behave and interact with them differently

And we can notice that with oop, you can create a data structure that behave as you want and based on fundamental data structures like lists, and define how they behave and methods to control them, and this class could be considered as a new personalized data structure

Stack indexes : 

![WhatsApp Image 2025-08-21 at 15 58 24_a677f0be](https://github.com/user-attachments/assets/01ba5283-6e89-409c-9b22-0483e25ef0a6)



## stacks in python : 


!!! : python does not have a built in stack data structure, they use simply a list then append and pop it, unlike other languages like c++

This is how we push and pop and get the peek value in a stack in python :

![WhatsApp Image 2025-08-21 at 16 45 01_2eba1fde](https://github.com/user-attachments/assets/17edb247-8e53-4b03-96ed-fc78f2802020)

<img width="893" height="418" alt="image" src="https://github.com/user-attachments/assets/8ee23b00-05ef-4b05-9e4e-78f09246e824" />


But as you see, we are simply using a list, which we can do some operations on it that go against the stack principles, so in python, we are dealing with a list while having the illusion of being a stack,when we say “stack,” we’re really talking about how we use the list, not what the list is







# Stack use cases : 



- Its useful to reverse thing, letsc say we want to reverse al list, we put this list elements in the stack then we empty this stack using pop, pop would return the top element deleted, we store it in a new list and by going over this process we will get the reversed list after the stack got empty



- Stack is widely used in the world of software developing, For instance:

Game dev, sort of actions are stored in a stack 

undo and redo principle, actually based on stacks


![WhatsApp Image 2025-08-21 at 16 35 09_9067f258](https://github.com/user-attachments/assets/3d81e946-e050-465f-ae21-82b70900f751)



- valid parentheses, revealed for us the first useful stack implementations and how they can make our solution way more simpler, it is a problem about checking if every parentheses opened has its correspond closing paranthese, so we ve simply made a stack, filling it only with opened paranthese, if we find its end we pop it from the stack, if we found a new opened parenth we add it to the stack, and we know that the peek parenthese which is the last one found, should be the first one closed, this is why stack is so useful here  

