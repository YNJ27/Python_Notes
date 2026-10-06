'''The enumerate function is a built-in function in Python that allows you to loop over a sequence
(such as a list, tuple, and even a string) and get the index and value of each element in the sequence 
at the same time.'''

marks = [12, 56, 32, 98, 12,  45, 1, 4]

#tidious method
index = 0
for mark in marks:
  print(mark)
  if(index == 3):
    print("Harry, awesome!")
  index +=1

# using enumerate:
for index, mark in enumerate(marks):
  print(mark)
  if(index == 3):
    print("Harry, awesome!") # will print this after knowing that harry is the topper

#Actually enumerate creates an enumerate object with tuples as its elements , containing index and value in it
print(enumerate(marks)) #will give something <enumerate object at 0x......>

#you can print it by creating its list :
print(list(enumerate(marks)))

'''And in the example 'using enumerate' we used the index and the value(marks) by unpacking the tuples'''


# using start parameter in enumerate:
#you can start the index from any desired number
for index, mark in enumerate(marks , start=1):
  print(mark)
  if(index == 4):
    print("Harry, awesome!") # will print this after knowing that harry is the topper


#Some examples with better presentation using f strings
marks1 = [97,85,92]
for index , marks in enumerate(marks1):
    print(f"{index + 1}: {marks}") 

