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















