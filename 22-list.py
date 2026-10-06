#LIST
#can have mixed datatypes
#mutable
#enclosed in square bracket

marks=[62,79,93,"fail",True] #can have any type of datatype

marks1=[67,72,["fail","full marks",0,"abscent"]] #can also contain another 
                                                # list in it
print(marks1)

marks2=[67,72,("fail","full marks",0,"abscent"),{"yug":30,"shlok":29}]
print(marks2)  #can also contain another dict,tuple,etc,in it


#mutation-
marks1[1]=27
print(marks1)


print(62 in marks) # to check wheter an item belongs to the list


#checking and also performing a task
if 62 in marks:
    print("yeah")
else:
    print("nooo")


#list comprehensions
#creation of a list using a for loop over any iterable like another list,
#string,tuple or using range and also a condition if required
list1=[i for i in range(5)]
print(list1)

#code for squares of even numbers
list2=[i*i for i in range(10) if i%2==0]
print(list2)

# Accepts items with the small letter “o” in the new list
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_O = [item for item in names if "o" in item]
print(namesWith_O)

#Accepts items which have more than 4 letters
names = ["Milo", "Sarah", "Bruno", "Anastasia", "Rosa"]
namesWith_length_more_than_4= [item for item in names if (len(item) > 4)]
print(namesWith_length_more_than_4)


'''
Slicing and Indexing is completely same as that of string
negative index and reverse slicing is also included
'''

marks3=[62,79,93]

marks3_sublist=marks3[:2] #slicing always generates a new list
                          #and the previous list is not changed
print(marks3_sublist)

marks3_new=marks3[:] 
print(marks3_new is marks3) # so it will give False because 
                            #though value is same but memory location
                            #allocated is different