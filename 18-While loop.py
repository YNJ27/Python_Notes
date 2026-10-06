#while loop 
'''Note:Unlike for loop ,while loop needs initialization(compulsorily) and also 
increament or decreament(generally) '''


#ex of while loop with increament
#
i=0
while (i<5):  #while loop excutes only if the condition is true
    print(i) 
    i+=1 
print("loop khatam ho gaya")


#another ex of while loop: (without increament)
#
num=int(input("please enter a number: ")) 
while num<=50:
    num=int(input("please enter another no: "))
print("your number is greater than 50")


# while can also be used with else
#
i=1
while i<11:
    print(i)
    i+=1
else:
    print("I just know numbers from 1 to 10")


# while loop with decreament

count = 5
while (count > 0):
  print(count)
  count = count - 1


#infinite while loop:

# i=1
# while i>0:   
#     print(i)
#     i+=1
'''don't execute the above code,it may harm your laptop.'''


#IMPORTANT QUESTION:............(There is no do-while loop in python)
#Emulate do-while loop in python

#Ex:1
print("actually this code is made to print numbers upto 10")
i=int(input("enter any number: "))
while True:
    print(i)
    if i<10:
        i+=1
    else:
        break

#Ex:2
# num=int(input("enter a number less than or equal to 10: "))
# while True:
#     print("you are on the way")
#     print(num)
#     if num<10:
#         num+=1
#     else:
#         print("you reached 10")
#         break
'''first check wheter it looks like a do while loop or not'''

