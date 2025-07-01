# this problem would be a nice opportunity to learn how to deal and manage dictionnaries in python 

### how to add elements to a dict :
the simplest way is just assign to the dict a new value accompanied with its key

hashmap["mathematics"]=22.5

--> {"mathematics" : 22.5}

### merging two dictionnaries :
a = {"name": "Wessim"}

b = {"language": "Python"}

a.update(b)

the result a={'name': 'Wessim', 'language': 'Python'}

### how to access and iterate through a dictionnary :
* ! you should always be aware of dict keys are the same as array indexes, it means when you write dict[0] it means you're asking for the value associated with the key=1

to iterate through a dict there's 3 ways :

* iterating through keys : 2 ways :
  - for key in dict : ----> this is the default one : !! by the way key is the name of the iterator, it could be named i, element, value, item etc....
  - for key in dict.keys() : ----> what is dict.keys() ??? it's a view that we can iterate, see its definition below

* iterating through value :
  - there's only one way to iterate a dict through its values, since the dict itself you can only iterate through its keys, so we use the view of its values which is dic.values() :
    for value in dict.values() : print (value), and as we've said value is just the name of the iterator

* iterating through items :
  - we use two iterators named key and value to iterate through the view dict.items(), then we have to adjust the printing mode to have an appropriate result :
    for key, value in my_dict.items():
    
    print(f"{key} → {value}")
    f'' used to adjust the print result in the string depending on (key and value) values every time


## what is a view : (every thing between "" "" is an AI definition)

""(AI ALERT) A view is a dynamic, read-only window into the data of a collection like a dictionary. It reflects the current state of the dictionary — so if the dictionary changes, the view updates automatically.""


a view is iterebale non indexed object in python : for example when we say dict.keys() : it's a view containing only the key values of the dict, we cannot make operations on it like sort etc... we can only print it or iterate through it adding to simple actions like :

print('a' in my_dict.keys())
the result would be true or false 
if you want to make operations using it you should transform it into a list or any other appropriate data structure, like this :
view = dict.keys()
other simple actions that are highly helpful : 

common_keys = d1.keys() & d2.keys()       --> {'b'}

common_items = d1.items() & d2.items()    --> {('b', 2)}

unique_keys = d1.keys() - d2.keys()       -->  {'a'}


for element in view : and starting to add its elements to the new data struct

- this is what dict.keys() view contains :
  my_dict = {'a': 10, 'b': 20, 'c': 30}
  
  values_view = my_dict.values()

  print(values_view)
  result : dict_values([10, 20, 30])

- this is what dict.items() view contains :
  my_dict = {'a': 1, 'b': 2}
  
  print(my_dict.items())

  dict_items([('a', 1), ('b', 2)]) : now you understand why do we need two iterators for it, its view containing tuples each tuple is composed of the key value first then the (value) value

  so views do have elements in all cases as we see but they cannot be indexed 
  


  







  

