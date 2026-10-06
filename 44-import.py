#WAYS OF IMPORTING PACKAGES AND MODULES

#1) Using import with the original name of the package or module
import math

# It will not only import the import the given module/package but will also import the one on which the original
# module or package is dependent

# Now you can use all variables and functions inside that module as its attributes or methods 
#Ex:
print(math.sqrt(25))  
print(math.pi)

#2) Using 'from' keyword - It is used if you want to import specific things from a complete module/package
#Ex:
from math import sqrt
print(sqrt(25)) #Now there is no need of the suffix 'math.'

#3) Using 'as' keyword - It is used if want to import a module/package using a different name
#Ex-1):
import math as m  #To decrease the coding effort
print(m.sqrt(25))

#Ex-2):
from math import sqrt as s, pi
print(s(25))

#Ex-3):It can also be used to descibe more about the module
import math as python_builtin_module_math
print(python_builtin_module_math.pi)

# Use of dir() - It will give you the list of all attributes,moethods,etc. present in that module/package
import math
print(dir(math))
print(type(math.tanh)) #You can use type function to understand what the desired thing inside a 
                       #package/module actually is?

#You can also import a self-defined file(module) and use functions and variables inside it
import examplefile44
print(examplefile44.e)
print(examplefile44.add(1,2))