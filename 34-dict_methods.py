#1)updating value of a particular key -

#A) update() - 
#It updates the value of the key provided to it if the item already exists in the dictionary,
#else it creates a new key-value pair. We can pass any no of key-value pairs.

info = {'name':'Karan', 'age':17 }
print(info)
info.update({'age':18}) #.......(updating an item)
print(info)

info.update({'DOB':2005}) #.......(Adding new item)
print(info)

info.update({'weight':65,'eligible':True, 'name':'Karan Luthra'}) #........(Multiple items with both addition and
                                                                           # updatation)
print(info)                                                                          

#Using two distinct dictionaries
'''Pehle division1(Toppers) me sirf Luv aur Kush the, aur division2(slow learners) me Shyam aur Ram the, badme 
hardwork karke Shyam aur Ram bhi division1 me aa gaye. At the end unke roll no.s bhi change kiye gaye'''

division1={'Kush':1,'Luv':2}
print(division1)

division2={'Ram':1,'Shyam':2}

division1.update(division2)
print(division1)

division1.update({'Ram':3,'Shyam':4})
print(division1)


#B)***Using the below given syntax - (It functions in the same way as update() do)
#It updates the value of the key provided to it if the item already exists in the dictionary,
#else it creates a new key-value pair. 

info = {'name':'Karan', 'age':17 }
print(info)

info['age']=18    #.....(updatation)
print(info)

info['DOB']=2005     #.......(Addition)
print(info)

'''Note - In this method you can't pass multiple items as keys and as values'''
info['weight','height']=65,5.6 
print(info) #....(here it will not create two items but will create a single item with tuples including keys and 
                # and values)

keys1=info.keys()
for key in keys1:
    print(type(key)) #......(type of the last key will be given as tuple)
#Same can be done for values 



#2) clear()- Will delete all the items in a dictionary and will give an empty dictionary
info = {'name':'Karan', 'age':17 }
info.clear()
print(info)

#3) pop()- It will remove the item whose key is passed as parameter
info = {'name':'Karan', 'age':17 ,'weight':65}
print(info.pop('name')) # . . . . .(returns the value of the key passed as parameter)
print(info)

#Note - If the key passed as parameter is not present in the dict. , it will return an error. To avoid it you can 
#pass a second argument which will be returned as a default value, if the key is not present in the dict.

info = {'name':'Karan', 'age':17 ,'weight':65}
print(info.pop('name2' , "Error occured"))
#               argument1    argument2
#                            (default value to be passed)


#4) popitem() - It will remove the last item of the dict.
info = {'name':'Karan', 'age':17 ,'weight':65}
print(info.popitem())  #.....(returns a tuple with key and value of the last item as its elements. You can check it
                            # by changing the syntax and using type())
print(info)


#5) del - If a key is passed then will remove that particular item. And if nothing is passed will delete the complete 
#dictionary

info = {'name':'Karan', 'age':17 ,'weight':65}
del info['name']
print(info)

info = {'name':'Karan', 'age':17 ,'weight':65}
del info
# print(info)  . . . (will throw error)


