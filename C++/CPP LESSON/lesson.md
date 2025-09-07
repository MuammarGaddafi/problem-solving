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


### name space : 

can define variables and functions and other structures in name space ? 

![WhatsApp Image 2025-09-06 at 16 12 12_e5ad3a6a](https://github.com/user-attachments/assets/7488618f-336a-4ac8-af67-764d415df933)

![WhatsApp Image 2025-09-06 at 16 12 25_3bff0f21](https://github.com/user-attachments/assets/2076d16b-9aa6-4808-a0e6-d9fcd412c978)

![WhatsApp Image 2025-09-06 at 16 12 36_b5f66d06](https://github.com/user-attachments/assets/c7f1bbb0-d95b-443c-9e08-589fac9b2f6e)

![WhatsApp Image 2025-09-06 at 16 13 00_9ae91f98](https://github.com/user-attachments/assets/6fc91b90-7a68-4631-b1d9-d40f2eda48a5)


lets see a practicle example : 

<img width="814" height="140" alt="image" src="https://github.com/user-attachments/assets/6555f22c-7915-49a1-8662-2d7942b61763" />

of course you can use a name of a variable or function more than one time as long as each name belongs to its own name space : 

<img width="283" height="183" alt="image" src="https://github.com/user-attachments/assets/27b96a0a-6b18-4659-a04b-35b82cfb300b" />

printing it in the main func : 

<img width="296" height="48" alt="image" src="https://github.com/user-attachments/assets/f6ae08bc-694b-46fe-b01c-3f7f8b7a8fdd" />


### USING  : what is the using prefix ?

it’s a language construct that serves multiple purposes depending on context. It’s often seen with namespaces

<img width="880" height="440" alt="image" src="https://github.com/user-attachments/assets/234d08ab-e1e2-4cce-a961-233d7d8975ec" />

<img width="901" height="320" alt="image" src="https://github.com/user-attachments/assets/8de645c7-488b-4c45-ab28-2975e22202a6" />

there still other use cases that are mainly related to OOP, we will see them as soon as we learn oop with cpp

<img width="335" height="262" alt="image" src="https://github.com/user-attachments/assets/4f71e5b1-ac91-4138-b300-9c4feae662a3" />


<img width="493" height="326" alt="image" src="https://github.com/user-attachments/assets/48f67e64-8a74-4a29-adba-ab95922bb4c1" />


### typedef and type aliases (we have seen those functionalities with the using key word and recommended to use it instead of typedef) : 


<img width="821" height="160" alt="image" src="https://github.com/user-attachments/assets/44057f2c-10e3-49da-a4c9-b3fc3fc7339c" />


first of all lets take this example of a data type : 

<img width="489" height="31" alt="image" src="https://github.com/user-attachments/assets/98770718-7d76-4404-ba97-133660d006c8" />

this is a template based data type in cpp

lets explain that data type : 

<img width="916" height="181" alt="image" src="https://github.com/user-attachments/assets/54459471-cbd3-4afb-9b7e-c3948f7329e7" />

this is how we would redefine or lets say rename that data type as a pairlist type : 

<img width="739" height="47" alt="image" src="https://github.com/user-attachments/assets/f9f512b1-212c-4629-af05-e82304e42d61" />

<img width="480" height="376" alt="image" src="https://github.com/user-attachments/assets/1fe11124-f357-444a-8622-1e768ed05ed0" />

this is how we use using instead : 

<img width="435" height="124" alt="image" src="https://github.com/user-attachments/assets/a435ed01-31d4-4de4-ac2f-46f8013c33ad" />



### type conversion : 

! you should know that you cant change the variable data type over the code after declaring it

<img width="827" height="119" alt="image" src="https://github.com/user-attachments/assets/f419e4b0-e6e7-4974-b72f-d4c6cdd43dd0" />


<img width="1077" height="684" alt="image" src="https://github.com/user-attachments/assets/00f82f1a-8756-47be-ac74-97cae577423a" />


the implicit conversion : 

<img width="479" height="364" alt="image" src="https://github.com/user-attachments/assets/f8d5fe00-c345-4613-971e-124c221da775" />

<img width="533" height="86" alt="image" src="https://github.com/user-attachments/assets/03bc98ee-67ba-4797-948f-9b7e8bea9946" />

explicit conversion : using the (datatype) to convert : 

<img width="542" height="395" alt="image" src="https://github.com/user-attachments/assets/669d4c57-b52c-4bfc-ac5d-2a56785e23bd" />


inmplicity with chars and values : 

<img width="246" height="90" alt="image" src="https://github.com/user-attachments/assets/869e1625-119d-4414-ba40-c49bf1d8eb78" />

x would get the character having 100 as an ascii code whiche is 'd' 

if we do the opposite : int x='d' : we will get 100 as a value of x (the ascii code of 'd')

explicity with char and values : 

<img width="312" height="43" alt="image" src="https://github.com/user-attachments/assets/d7e6ffc0-d41d-49bd-abaa-172e7138e1c2" />

we would get 'd' as an output

divisions and math opearations : type conversion : 

here we would get an int result (but ending with .000 because the variable stored in is a double) because we are using an int division between two ints variables

<img width="383" height="102" alt="image" src="https://github.com/user-attachments/assets/d23a9243-eeda-4248-9d5d-00630da2fc01" />

if one of those variables is a double, then the result would be decimal , but you should be aware that the result then would be processed to fit the assigned to variable type (if it is we would store the result as an int and if it is a double then the result stored as a double)

<img width="904" height="378" alt="image" src="https://github.com/user-attachments/assets/875c4cad-6624-4330-96ea-8d538c14e76b" />


<img width="474" height="23" alt="image" src="https://github.com/user-attachments/assets/f99b96df-b017-4570-bacf-f11fe5b049b1" />


the summary : 

int x = ..... (what ever is the value, it would be stored as an int) 
double x = ...... (what ever is the value, it would be stored as a double, if it is an int it would be under this format : x.0)

int x = 2/1.0 --> since one of them is float then the result is a double(it would be 2.0) but the variable is declared as an int so x would have 2 as a value


char x = 33/11 --> x would be the character with ascii code = 3 , if the division result is not available as an ascii code then an error would raise (like 33.00/23.00) (33/22 is an int division because it is a division of two ints so the result would be relevant)

int x = 'A' --> x=65 


### here you can find the reference book of cpp and all what you need about it related to functions and syntaxe : 

lets take the example of math functions, here is the section where you can find any thing about math libary of cpp

<img width="1253" height="680" alt="image" src="https://github.com/user-attachments/assets/1e359959-1f3f-4c94-9da3-d7fcaaaf3918" />



### conditional statements : 

<img width="654" height="355" alt="image" src="https://github.com/user-attachments/assets/aa6b75bd-0a78-42db-b9b8-399409a9a289" />


### switch statement : 

the switch is to apply a procedure depending on the appropriate case, the case is what the of the switch variable could be : 

!!! at every case you should add the break statement, cz if the case is valid, the program quit the loop, otherwise the switch bloc would never come to an end

the default case : 

you don't need break statement with default, because the default is typically the last case in the block so the code would quit automatically, but you still can add it 

<img width="492" height="431" alt="image" src="https://github.com/user-attachments/assets/ad74d92d-bf8c-403b-a0f5-6445fecde150" />


<img width="617" height="371" alt="image" src="https://github.com/user-attachments/assets/43d1fc39-0803-4df4-b638-5310a8d15c5c" />


lets make a calculator with switch : 


<img width="658" height="509" alt="image" src="https://github.com/user-attachments/assets/f2008110-c456-4bf8-bb31-9d3fbb4aee3d" />


<img width="719" height="576" alt="image" src="https://github.com/user-attachments/assets/879c8905-7b34-464c-9bbb-9c28b0b6f9cd" />


### string methods : 

the getaline : 

<img width="416" height="38" alt="image" src="https://github.com/user-attachments/assets/e796c6fe-1eb8-43c1-bbc2-daa3466e88a2" />


<img width="927" height="234" alt="image" src="https://github.com/user-attachments/assets/150005d1-83fd-40e3-b6f2-fc2b7800702a" />


difference between reading a string input and declaring a string variable : why we need getaline just for input :


<img width="927" height="681" alt="image" src="https://github.com/user-attachments/assets/c96d0dcb-249b-4dad-b75d-28820b8b586d" />



mystring.clear --> clear the string

mystring.append() --> append the string

string element access : you can access with mystring.at(0 ) or mystring [ 0 ]  

mystring.insert(index,element to insert)

mystring.find(the element we want to find) --> returns the index of the element

mystring.erase(debut,end) --> the bloc we want to erase 

here you can find more useful tools for strings : 

<img width="852" height="685" alt="image" src="https://github.com/user-attachments/assets/ae8f8e82-b316-4a8f-af8e-26ebced89bcd" />




## THE LOOPS 


### while and do while loops : 

they don't need so much presentation, you know them well, they are like repeter jusqua and tant que in algorithm, the do while would always run the block of code inside the loop at least once,

a while loop to read an unempty string : 

<img width="601" height="289" alt="image" src="https://github.com/user-attachments/assets/72b0694f-78e7-4310-bd52-f0e6dd2867d2" />


do while : 

<img width="753" height="87" alt="image" src="https://github.com/user-attachments/assets/99c62d1d-49df-4415-9c79-402038e3b838" />


<img width="518" height="238" alt="image" src="https://github.com/user-attachments/assets/f77f3685-36c2-4716-b79c-d1a8f42f6f5a" />


### for loops : 

<img width="543" height="225" alt="image" src="https://github.com/user-attachments/assets/c76aef9e-1519-432a-8f40-dfe2c0d5b45a" />

so the for loop takes the first value that it would start from, the condition of running (actually it is the ending condition) and the incrementation (the steps to move by)


### break and continue ( used with loops) : 

break : you already know it, you quit the loop immediately 

continue : used to skip an iteration, lets take this example with for loop : 

<img width="415" height="200" alt="image" src="https://github.com/user-attachments/assets/06acc6aa-c601-4863-87c7-f58bee929959" />


<img width="985" height="652" alt="image" src="https://github.com/user-attachments/assets/8f272113-8e01-4f36-8a49-83eb1dc261f7" />

do you see, the programm has skipped the 13th iteration












