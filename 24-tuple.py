'''Tuples are immutable'''

tup1=(1,2,"yug",True)
print(tup1)
#same as list tuple can also consists of mixed datatypes

#INTERSTING POINT
#1)
tup2=(1)
print(type(tup2))

list1=[1]
print(type(list1))

#2)
tup3=("Raj")
print(type(tup3))

list2=["Raj"]
print(type(list2))

'''***single item list is a list , but a single item tuple
is not a tuple. It is considered as the dataype of that
individual item***'''

#SOLUTION-
tup4=(1,) #Give a comma at the end, if want to form a 
          #single item tuple
print(type(tup4))

tup1=(1,2,"yug",True)
# tup1[3]= False .......will throw error because tuples are 
                       #immutable


#checking presence
print(2 in tup1)

#checking presence and carrying out task accordingly
if 2 in tup1:
    print("2 is present in tup")
else:
    print("2 is absent in tup")
    