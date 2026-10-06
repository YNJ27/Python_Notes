name="Yug Nitin Jain"
print(len(name))

#SLICING OF STRING
'''***the arguments must be of int datatype***'''

'''Note-slicing returns you a new string , because we know that strings are
immutable''' 

print(name[0:5]) #the first digit in the square bracket-to start from this index
                 #it will end at the index 'second digit - 1'  

# explaining the 'Note' statement                 
name2=name[0:5]
print(name2)

print(name[0:]) #if no second digit is mentioned,it will consider length of string
print(name[0:len(name)]) #identical output as that of above 
print(name[:]) #IDENTICAL output as above

print(name[:3]) #if no first digit is mentioned,it will initiate with 0
print(name[0:3]) #identical output as that of above

#***Slicing in reverse order***:
print(name[-1:-15:-1]) #important example 1
#Note:in reverse order the index of 'Y' is -14

#important example 2
print(name[::-1]) # it will by default consider first argument as '-1'
                  # and second argument in such a way that it will 
                  # complete the whole string                

#important example 3
print(name[-1:-14:-1]) #the concept of 'second argument-1' is wrong
                       #it actually ends one number before the second
                       #argument
                    
#important example 4
print(name[-1:0:-1]) #note you can use any type of argument 
print(name[13:0:-1]) #i.e. either the one used in normal order
                     #or the one used in reverse order
"now here the index 0 was for 'Y',so it stopped till 'u'."
"as both 13 and -1 is for 'n',it will give the same output"

#important example 5
#print(name[-1:-1:-1])  #---now you may think that when 2nd argument was 0
                        #we were getting output excluding 'Y'.So if we 
                        #used -1 it may work.
'''but this -1 refers to index , and if you understand it properly,you will
understand it is a error'''

#important example 6
print(name[-1:-16:-1]) #though you entered a number greater than the one required 
                       #to slice the whole string, it will stop as soon as
                       #the string is completed