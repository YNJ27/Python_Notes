# SETS 
'''
1) We can insert items with mixed datatypes in a set (similar to lists and tuples) 
'''


'''
2)It doesn't allows duplicate items, so whenever you want that items in a collection should not repeay , you 
should use sets
'''
set1={1,2,"yug","dev",76,2}
print(set1)                 # 2 will not get printed 


'''
3)It is also an unordered collection.So you can not access the items using index
'''
set2={"om","vansh",22,20}
print(set2)     # If you ran the code multiple times , everytime a different order is displayed

# print(set2[1]) ..... throws error 


'''
4)Items in a set can be accessed using a for loop
'''
for val in set2:
    print(val)


'''
5) How to define an empty set
'''
#Wrong method-
set3={}
print(type(set3))  #It is actually a dictionary

#Correct method-
set4=set()
print(type(set4))


'''
6)sets are unchangable.It means that we can't change the value of an item (replacement). But we can add and 
remove items which will be teached later
'''
set5={2,7,8,4,2}

# set5[0]=1 ..... will throw error

for val in set5:
    val=100

print(set5) #set5 will still remain unchanced