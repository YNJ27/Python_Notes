#String Formatting

#A) Previously used method
#1) Method 1:
# name="Vansh"
# place="Dungri"
str1="{} is my brother and he is from {}"
name="Vansh"
place="Dungri"
print(str1.format(name,place))  # format is a method of class string

print(str1)       # if you want to print your template string itself 

#2) Method 2:
str1="{1} is my friend and he is from {0}" #Now if you forgot to pass the parameters in format in a proper order
                                           #you can give their respective indexes to the appropriate curly brackets
                                                                   
name="Aditya"
country="US"
print(str1.format(country,name)) 
#                   0       1

'''But in both these methods you have to take care of the order. So python introduced a new thing called fstrings, it 
is applicable in all python versions from 3.6'''

name="Shivaji Maharaj"
name_of_empire="Maratha"

str2=f"{name} was the king of {name_of_empire} empire"

print(str2)

str_1=f"{{name}} was the king of {{name_of_empire}} empire"

print(str_1) # If you want to print your template/raw fstring as it is. 


''' There is another type in the previously used method where you can get rid of order , but it has some drawbacks'''

str3="{name} is my brother and he is from {place}" # Take care of the syntax

print(str3.format(name="Vansh",place="Dungri")) #But here everytime you have to write the variable along with its value
                                                #like key-value pairs 


'''some more uses of fstring'''
print(f"{2*30}")   # we can use it in single statement as well



'''some other applications of formatting.Mainly used and applicable for float'''
#m:a.bt
#m is for index of the parameter passed in format()
# here a = minimum total digits to be present in the string
# b = no of digits to be present after the decimal point, also called as precision
     #it can't be applied for integer datatype (i.e here 'd')
# t = type of variable
        #for example : s - string
        #              d - integer
        #              f - float              
        #              and few more which can be found on geeks for geeks 

#Method A - Using format:
txt="The toy is actually for {1:1.2f}, but I can give it to at a final price of {0:1.4f}"
print(txt.format(3.141592,4.919))  # Precision also gives you a rounded off value

txt2="The toy is actually for {mrp:1.2f}, but I can give it to at a final price of {sp:1.4f}"
print(txt2.format(sp=3.141592,mrp=4.919))  # using key value pairs,here instead of index keys are used

#Method B - Using fstrings:
mrp1=5.919
sp1=4.141592
txt3=f"The toy is actually for {mrp1:1.2f}, but I can give it to at a final price of {sp1:1.4f}"
print(txt3)

'''Note- In both method A and B you have to use appropriate suffix for appropriate datatypes
         i.e. you can't use 's' for integers or float, also you can't use 'd' for float and string 
         But the only thing you can do is you can use 'f' for integers '''




'''Another method of formatting strings'''
#Using % 
#Again 1) %s - string
        # %d - integer
        # %f - float  
#Again the same thing i.e  'a.bt' (Note- this thing is mainly used for float only('f'))
# here too you can't use precision (i.e. b according to the above formula) for integer i.e 'd'.

# Basic example to understand syntax and use
name="Yug"
age=18
s1="%s is %d years old"%(name,age)
print(s1)

#example using precision and all for floating point numbers
num1=22
num2=7
num3=3.1428
s2="%d / %d = %1.3f"%(num1,num2,num3)
print(s2)

'''Note - Here 's' can be used for any datatypes like list, tuple, and (most importantly) even float and integer 
          But you can't use 'd' , 'f' for any other datatypes. 
          Yes but you can use 'f' for integers ''' 

