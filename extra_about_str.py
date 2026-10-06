str1="yug"
#We know that strings are immutable, but what does it exactly mean
#it means that you cannot cary out the following type of operations
#1)str1[0]="d"
#2)str1[1]="e" , etc.

#but you can completely change the value, for eg:
str1="dev"
print(str1) #it will print dev not yug 
 
#also you can carry out concatenation as shown in 'imp_str_problem'
#and 'imp_str_problem2'. check them out they are tricky



#Note- important information about single vs multiple line strings

#single line strings can start from any column
#Ex-1)

#code to print my name
print("Yug Nitin Jain") #Actually my surname is 'Gandhi'

#so no error is given by any comment on line 21,22

#Ex-2)

'''write a code to print your brothers name'''
print("Om Sunil Jain") '''Sunil is my uncle's name'''

#note- here the comment on line 29 will throw an error
#because multiple comments should start from the first
#column only