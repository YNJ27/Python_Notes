# for loop:
#we can iterarte for each value of the following datatypes
#string,tuple,list,set,dictionary
#note: integer and float datatype is not iterable

list1=["yug","dev","om"]

for val in list1:
    print(val)
    for char in val: #(while using nested for loops,names of
        print(char)  # two variables must be differnt.for 
                     # example val and char are two 
                     # distinct variable names)

#use of range-
for i in range(5): #Note:the value of i is initiated to 0.
    print(i)       #and like slicing it ends at n-1,
                   #where n is the given argument

'''***arguments of range must be integers***'''

#use of range with step - EX:-printing odd numbers from 1-9  
for i in range(1,10,2):   #(start,end,step)
    print(i)

#reverse iteration
for i in range(10,0,-1): #***actually it not ends at n-1 
    print(i)             #but it ends at a number before the 
                         # given second argument.Now as we are
                         #iterating in reverse order,it will end
                         #at 1.(keep the above concept in your mind,
                         #and forget the previous concepts)



