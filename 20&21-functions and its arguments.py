
#2)def factorial(num):
#    if num==0:
#        a=print("The factorial of 0 is 1")
#        return a

#s=factorial(0)
#print(s)

'''Functions'''
#function to find the geometric mean

# 1) When you only call the function
def geometric_mean(a,b):
    g_mean=(a*b)/(a+b)
    print("Geometric mean of given numbers is",g_mean)

geometric_mean(9,10)    #here the function will only execute all the commands

#2)a) When you make use of return:(return is generally used to store the output of a function for further use)
def geometric_mean(a,b):
    g_mean=(a*b)/(a+b)
    return g_mean        # return ka matlab vapas chalejao is value ko leke. 

s=geometric_mean(9,10)   #jab hamne function ko call kiya,function g_mean ki value leke vapas chala gaya
                         #Aur vo value hamne 's' me store kardi
print(s)   

#b) Another way to just get the output:
def geometric_mean(a,b):
    g_mean=(a*b)/(a+b)
    return g_mean 

print(geometric_mean(9,10))

#Note: when youn don't use return but if you use the same printing syntax as that of the second example,
#function will return 'None'. check the third example
#3)
def geometric_mean(a,b):
    g_mean=(a*b)/(a+b)

s=geometric_mean(9,10) 
print(s)

#4)using more than two return functions(always the first return is considered)
#a)
def geometric_mean(a,b):
    g_mean=(a*b)/(a+b)
    return 7 
    return g_mean        #actually it is a useless code 

s=geometric_mean(9,10) 
print(s)

#b) it is actually used when if else is involved
def factorial(num):
    if num==0:
        a="The factorial of 0 is 1"
        return a
    elif num==1:
        a="the factorial of 1 is 1"
        return a
    elif num>1:
        prod=1
        for i in range (2,num+1):
            prod=prod*i
        a=prod
        return a

v=factorial(5)
print(v)

#function arguments:
#1) Default arguments:
#A) when you pass any arguments
def average(a=9, b=1):
    print("the average is",((a+b)/2))

average() # it will consider the default values of a, b i.e here 9,1

#B) when you pass some arguments 
#1.passing both a and b
def average(a=9, b=1):
    print("the average is",((a+b)/2))

average(4,2) #it will now consider value of a,b as 4,2 respec.

#2.passing any one
def average(a=9, b=1):
    print("the average is",((a+b)/2))

average(1) #it will consider a as 1(new),while b as 1 (default)
average(b=9) #it will consider b as 9(new),while a as 9 (default)

#2)keyword : parameters are passed in key-value pairs form while calling 
           #the function. thus order in which the parameters were written
           #in the function defination dosen't matter
def average(a=9, b=1): #default
    print("the average is",((a+b)/2))

average(b=3,a=11)

#3)Required - 
#A)using key-value type  
def average(a, b): #required - matlab a aur b ki value denihi padegi
    print("the average is",((a+b)/2))

average(b=3,a=11) 

#B)if not using key-value format , you have to pass the arguments 
#  in the correct order and also the number of arguments should match
#  with function defination
def average(a,b): #required
    print("the average is",((a+b)/2))

average(3,11) # you have given a as 3, b as 11

#C)few required few default:
def average(a,b,c=2): #required-a,b
    print("the average is",((a+b+c)/2))

average(3,5)

#4)variable length argument- you can give n number of inputs 
#a)Tuple-
def average(*nums):
    print(type(nums)) #it generates a tuple in which you can provide 
                      #any no of inputs
    sum=0
    for i in nums:
        sum+=i
    print("average =",sum/len(nums))
    
average(2,3,4)
average(5,7,9,1)

#b)Dictonary- if you want to give arguments in key value pair form 
            # without worring about order
def name(**name):
  print(type(name)) #it generates a dictionary
  
  print("Hello,", name["fname"], name["mname"], name["lname"])
# print(name)

name(mname="Buchanan", lname="Barnes", fname="James")
