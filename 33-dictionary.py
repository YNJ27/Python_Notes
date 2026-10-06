#Dictionarys can also store variables of different types

info = {'name':'Karan', 'age':19, 'eligible':True}
#        key    value

print(info)

#1) Accessing single value -
#A)Method I-
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info['age'])

#B)Method II-
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.get('eligible'))

'''Difference between the two methods is that if a key which is not present in the dictionary is passed ,Method I
will throw an error(KeyError) but Method II will not, it will instead return None.Thus we can use these based on
whether we require error or not'''

info = {'name':'Karan', 'age':19, 'eligible':True}
# print(info['age1']) .......(will throw error)

info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.get('age1'))


#2)Accessing all the keys of a dictionary-
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.keys())


#3)Accessing all the values of a dictionary -
#A) Method 1-
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.values())

#B)Method 2-
for key in info.keys():
    print(info[key])

#Method 2 can have a little advance but similar usecase as the below given example
for key in info.keys():
    print(f"The value corresponding to {key} is {info[key]}")


#4)Accessing key-value pairs -
info = {'name':'Karan', 'age':19, 'eligible':True}
print(info.items())

#A basic use-case 
for key,value in info.items(): # .......(two variables can be used for info.items() only .It can't be done with info
                                        # directiy)
    print(f"The value corresponding to {key} is {value}")

