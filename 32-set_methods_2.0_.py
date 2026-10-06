'''Note- set_methods_1.0 is written in a word file (location - desktop)'''

#9) add()-
#will add a single item in the orignal set

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.add("New York")
print(cities)

#Output:
#{'Tokyo', 'New York', 'Delhi', 'Madrid', 'Berlin'}


#10)update()-
#If you want to add more than one items in the existing
#set, you have to first make another set will new items
#and then make use of update method, as teached before

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities2 = {"Japan","Malasiya"}
cities.update(cities2)
print(cities)

#Output:
#{'Madrid', 'Tokyo', 'Malasiya', 'Berlin', 'Japan', 'Delhi'}


#11)remove() and discard() - 
#Both are used to remove a single item from the given set

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.remove("Madrid")
print(cities)

#Output:
# {'Berlin', 'Delhi', 'Tokyo'}

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.discard("Madrid")
print(cities)

#Output:
# {'Berlin', 'Delhi', 'Tokyo'}

'''
Note - The main difference between remove and discard is 
that, if we try to delete an item which is not present in
set, then remove() raises an error, whereas discard() 
does not raise any error.
'''

# cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
# cities.remove("Seoul") .............(throws error)
# print(cities)

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.discard("Seoul")   #.....(doesn't throw error)
print(cities)

#Output: - (No change is made with cities)
#{'Madrid', 'Tokyo', 'Delhi', 'Berlin'}

'''
Note- Now you may think that discard() is more useful than
remove() as it doesn't throw error, but it is not the case
Some times we really need errors. Also sometimes if error
doesn't occur and if further lines are executed than that
mistake may affect the results of the following code.
'''


#12) pop()- Same as in lists , it removes the last element
#in the set , but the catch is that we don't know which 
#item will get removed .But you can access the removed
#element as pop returns it.

#Note- You may or may not store the value returned by pop,
#depending upon whether you want to access the removed
#item or not . 

'''
*****Note- This thing is similar to just calling function
and storing the value returned by it in a variable.This is
because at the end methods are functions drfined in a 
class. And this thing can be implemented on any method,but
each method may or may not return a value
'''

#(I) - Not storing the value returned by pop()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.pop() 
print(cities)

#Output:
# {'Delhi', 'Madrid', 'Berlin'}


#(II) - Storing the value returned by pop()
cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
item = cities.pop()
print(cities)
print(item) #. . . . (accessing the removed item)

#Output:
# {'Delhi', 'Madrid', 'Berlin'}
# Tokyo


#13) del - it isn't a method but it is a keyword. And it 
#deletes the complete set it self

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
del cities
# print(cities) ....(will throw error as cities doesn't
#                    exist now)


#14) clear() - if you don't want to delete the set , but 
#if you just want to remove all the items in the set then
#you can use clear() method.

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
cities.clear()
print(cities) #....(will give you an empty set i.e 'set()')



#15)A) Checking the presence of an item in the set

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
print("Berlin" in cities)


#B) Checking and executing a task accordingly

cities = {"Tokyo", "Madrid", "Berlin", "Delhi"}
if "Kabul" in cities:
    print("Kabul is present in cities set")
else:
    print("Kabul isn't present in cities set")