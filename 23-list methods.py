#list methods

#note - try to use the given syntax otherwise error may get generated

list1=[1,3,4,5,7,9]

#1) append() - adds an element to the end of the list
list1.append(10) #wrong syntax- print(list1.append(10))
print(list1)

#2) sort() - arranges the numbers in list in an ascending order
#Note - actually sort() makes use of unicode code points
list2=[2,7,3,8,6]
list2.sort()
print(list2)

# we can also arrange the numbers in a descending order
list2.sort(reverse=True)
print(list2)

#we can also sort words alphabetically
colors = ["voilet", "indigo", "blue", "green"]
colors.sort()
print(colors)
# here too we can 'reverse=True' the colours in anti-alphabetical order

#3)copy() - 
#importance of copy explained in the below example
l=[2,3,4,5,6]
m=l
m[0]=1
print(l) # now you may think that as we created a new list m 
         # and made changes in m. So there should not be any changes
         # in l(previous list)
'''what actually happening is you are just providing a new reference 
for the same list l present in the memory.'''

#now if you want to carry out operations on a list but also want the 
#orginal copy with you. then use copy()
l1=[2,3,4,5]
m1=l1.copy()
m1[0]=1
print(m1)
print(l1)

#4)extend-puts the values of one list in the end of another list
l2=[100,200,300]
m2=[400,500]
l2.extend(m2) # *
print(l2)     # *

#we can also add the above two lists without altering the first list
k=l2+m2 #using concatenation
print(k) # to get the same output first comment out the lines in
         # which exten command is used

li3=[1,2,3,4,1,5,6,2,1,6]
#5)index - gives the index of the "first" occurence of the defined item
print(li3.index(2)) 
 
#we can also find the index of further occurences using slicing
print(li3.index(2,2,10))

#6)count - gives the number of times a item occured in the list
print(li3.count(1))

#7)insert - can insert an item to the specified index
li3.insert(7,"CR-7") # first argument-index where you want to insert the item
                     # second argument-the item to be entered
print(li3)

#8)reverse - reverses the order of the list items
li4=[2,4,6,8]
li4.reverse()
print(li4)

#9)pop()-removes the element at the specified index
li5=[1,3,5,7]
li5.pop(0)      # pop() returns the value of the deleted item . To check use the syntax - print(li5.pop(0)) instead 
                # It will return 1
print(li5)


li5.pop() # but if no index is mentioned python implicitly
          # removes the last item
print(li5)

#10)remove() - removes the specified element
li6=[1,3,5,7,9]
li6.remove(3)   # unlike pop remove return None.
print(li6)


#you can also make use of the index
li6.remove(li6[0])
print(li6)

# li6.remove() ......will give error, because we have to 
                    #compulsorily pass an argument,unlike 'pop()'
# print(li6) 

#11) del - deletes the element at the specified index, or few elements if used slicing ,
          #and if nothing is passed then deletes the complete list
li7=[1,3,5,7]
del li7[1]     # deleting a single item
print(li7)

li8=[2,4,6,8]
del li8[1:3]   #deleting a few items using slicing
print(li8)

del li7        #deleting the complete list
#print(li7) .....will throw error as now li7 doesn't exist