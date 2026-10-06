# # if else 
# '''conditional operators:1) >  
#                          2) <  
#                          3) >= - greater than or equal to
#                          4) <= - less than or equal to
#                          5) == - equal to 
#                                  (Note: don't use = ,it is to assign
#                                  values to variables)
#                          6) != - not equal to '''
# b=int(input("enter a no:"))
# print(b>=20)
# print(b<5)
# print(b==10)
# print(b!=10) #we get outputs in boolean datatype

# '''so if-else statements check the truthness of the condition.If the condition 
# is gives True , the block statements are executed,otherwise the interpreter
# directly jumps on the line below the whole block'''
 
# #Eg1: only if and else
# a=int(input("enter your age:"))
# if (a<18):
#     print("you cannot vote")
# else:                        # note you cannot apply condition to else
#     print("you can vote") 
# print("Have a good day")
# '''Note: indentation represents that the following statements are inside
#         if or else i.e. areblock statements.Now as the last statement is 
#         not indented,so it is not a part of else.So it will be executed
#         everytime(if ke statements execute hone do ya else ke)'''

# #eg2: if-elif-else(A)
# #code to check whether the number is positive or negative
# b=float(input("enter any number: "))
# if (b<0):
#     print(b,"is negative")
# elif (b==0):
#     print(b,"is neither negative nor positive")
# else:
#     print(b,"is positive") 

# #eg3: if-elif-else(B)
# c=int(input("enter a number:"))
# if (c<0):
#     print(c,"is negative")
# elif (c==0):
#     print(c,"is neither negative nor positive")
# elif (c==7):
#     print("CR7 and Mahi") # try once
# else:
#     print(c,"is positive") 
# '''now in this code when you provide 7 it will satisfy the third condition
# and the block statement will be printed. But though it is positive the fourth
# condition will not be checked.'''

# '''Because in if-elif-else statements only the block statements of the first
# condition which is satisfied is executed.The interpretur directly jumps to
# the line without any if-elif-else after executing the satisfied condition.'''

# #eg4: nested if-else (better solution for above eg)
# d=int(input("give a no.: "))
# if (d<0):
#     print("no is negative")
# elif(d==0):
#     print("number is neither positive nor negative")
# else:
#     print("number is positive")
#     if (d==7):
#         print("and also special.CR7 and MAHI")
#     else:
#         print("but not special")

num = -3

if(num < 0):
    print("The number is negative")
elif num==0:
    print("The number is zero")
else:
    print("The number is positive")