name="Yug"
name1='''Yug'''
name2='Yug'  #in python string can be enclosed is single,double,triple quotes
print(name,name1,name2)

#lets say you want to print - He said,"Yug is a good boy"

#print("He said,"Yug is a good boy"" )  - THROWS ERROR

print("He said,\"Yug is a good boy\"") #FIRST WAY
print('He said,"Yug is a good boy"')   #SECOND WAY

#string is an array and you can access any of its character
fruit="Apple"

#Note-PYTHON ALWAYS STARTS COUTING FROM 0
print(fruit[0])
print(fruit[1]) #This 0,1,2,etc are called index-(GIVES POSITION)
print(fruit[2])
print(fruit[3])
print(fruit[4])

#We can also access the characters in reverse order
print(fruit[-1]) #the last character has the index '-1'
print(fruit[-2])
print(fruit[-3])
print(fruit[-4])
print(fruit[-5])

#multiple line strings are written only in tripple quotes

#Myinfo1="Yug dada
# ghar ka shehzada
# engineering karta"
# print=(Myinfo1)       -THROWS ERROR

Myinfo2='''Yug dada
ghar ka shehzada 
engineering karta'''
print(Myinfo2)          #proper method

#you can use for loop to print each character of your single/multi line string
for character in fruit:
    print(character)

for character in Myinfo2:
    print(character)    
