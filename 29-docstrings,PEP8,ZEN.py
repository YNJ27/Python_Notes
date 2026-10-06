'''
Docstrings are defined just after the header of a function or method or module or class.
'''

def square(n):
    '''Takes in a number n, returns the square of n'''
    print(n**2)

square(5)

'''Note - Don't confuse between comments and docstrings. Comments are completely ignored by the interpretur
While docstrings can  be accessed and even displayed . These are used to document our code '''

#Docstrings are only written in between triple sinle(''' ''') or double(""" """) quotes

#Accessing the docstring
print(square.__doc__)

#If you wrote a string literal below even one line of the body

def geometric_mean(a,b):
    g_mean=(a*b)/(a+b)
    '''It will take in 2 variables and will 
print their geometric mean'''
    print("Geometric mean of given numbers is",g_mean)

geometric_mean(9,10)

print(geometric_mean.__doc__) #It will return None , because docstrings can only be defined just after the header 
                              # or just before the body


#PEP8:
'''PEP 8 is a document that provides guidelines and best practices on how to write Python code.
   The primary focus of PEP 8 is to improve the readability and consistency of Python code.
   PEP stands for Python Enhancement Proposal, and there are several of them. A PEP is a document that describes
    new features proposed for Python and documents aspects of Python, like design and style, for the community'''

#Zen of python : use first 'python' in terminal and then 'import this'  
'''it is nothing but a poem describing good coding practices'''

