# LETS LEARN C + +    +++++++++++++++++++++++++

lets take an eye on the small deatils of cpp : 

## FIRST OF ALL, why the main function in cpp returns an int, exactly a 0 ? : 

![WhatsApp Image 2025-09-03 at 01 36 27_a8fabfbf](https://github.com/user-attachments/assets/ead26f75-4936-4e43-8b5d-af94dd646e77)

For example for shell scripting :

./myProgram

if [ $? -eq 0 ]; then

  echo "Success!"
  
else

  echo "Failure!"

Here, $? captures the return value from main(). And that’s why it’s not just a number, it’s a signal of success, a contract with the OS


## IOstreams, their syntax and what are streams ? :

* std::cin and std::cout : !!!!!!! they are objects, not functions as many think :

<img width="894" height="204" alt="image" src="https://github.com/user-attachments/assets/0094d51c-2658-49ee-8f58-fcf5201d663e" />

These are global objects defined in the <iostream> header and live (classified) in the std namespace. They are instances of classes that define how data flows in and out


* what is a stream in c++ ? :

streams is a new term that we come accross when learning cpp, we ve never seen this before in python, streams is not a class or data structure as many think, they are just a type of classification :

streams represents the objects that we use as a pipeline, like the input and output objects, so the stream is a pipeline which data flows through

![WhatsApp Image 2025-09-05 at 21 25 41_858d8905](https://github.com/user-attachments/assets/3bd960c0-faeb-4cbb-8784-030d7317dd30)

![WhatsApp Image 2025-09-05 at 21 26 39_47b5280a](https://github.com/user-attachments/assets/43b0bca7-d942-488d-a0cb-ff984f521848)

* the << and >> we use with the streams : 

if those operators are not overloaded (their functionality changed), so they are opearators exclusively used with the streams : 

they move data into or out of streams

- (<<) is the insertion operator (used with std::cout) : we would insert to the output stream to print it

- (>>) is the extraction operator (used with std::cin) : we would extract the input of the user

<img width="953" height="144" alt="image" src="https://github.com/user-attachments/assets/b30a8391-8554-4d6c-823f-e07e942491da" />









## the std : 

the std is a namespace ( a namespace in cpp is like a module in python(but it is mainly for naming and defining for more clarity !!), a namespace is very helpful for naming conflicts, it is a container that helps to avoid those conflicts and to tell you what family does this item belong to)

the std namespace, is a name space regrouping all the standard items (they may be classes, variables, functions etc...) that we need

the header (the included file ) : 

<img width="881" height="457" alt="image" src="https://github.com/user-attachments/assets/f0cc3cd6-5923-4c26-aff6-738756274867" />



## the scope resolution (::) : 

 the scope resolution operator is most famously used with namespaces, but it’s far from namespace-exclusive. It’s a versatile tool that tells us what does the name belong to 

 scope res my be used to access : 
 
 * global variables : 

<img width="920" height="433" alt="image" src="https://github.com/user-attachments/assets/bbf138dc-12b0-4252-be02-5633382a68f5" />

* the other use cases will be revealed when you learn CPP OOP

<hr> <hr> <hr>


now lets dive deeper into more fundamental and bigger essentials of cpp : 

### why the string class constructor (type) belongs to the std name space not rawly used like int char etc ... : 

![WhatsApp Image 2025-09-05 at 22 29 20_cdfd2821](https://github.com/user-attachments/assets/1f2485ba-5188-4e8a-9c95-f5bea62083f2)


### std::cout syntaxe : 

print(a,b) --> std::cout a << b : first of all, any variable or item given to the cin to be printed, would be printed in line, so you should use the break tools if you want to print the item on new line

concatenation of strings is possible in cpp : std::cout << name1+"+"+name2+"= love" 

* you can print also in this way since the std out prints the outputs on same line : std::cout << "hello " << name :

but its better to print it with concatenation to be considered as one message : std::cout << "hello " + name 





