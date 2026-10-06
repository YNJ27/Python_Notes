#It is used to execute a code everytime irrespective of whether the code inside 'try' gets executed or the code
#inside 'except' gets executed 

#Ex-1:
try:
    i=int(input("Enter a number: "))

except:
    print("Some ERROR occured")

finally:
    print('ada pada kaun pada , bapuji ka ghoda pada')


#Ex-2: Now you may think that why I should I use 'finally', because the same work can be done by just writing 
#      the code below the 'except' block.
try:
    i=int(input("Enter a number: "))

except:
    print("Some ERROR occured")


print('ada pada kaun pada , bapuji ka ghoda pada')


#Ex-3: But it is mainly used in case of functions.

#Case1:Without using finally keyword 
list1=[1,2,4,8,16,32]

def finding_a_value_from_list(list):
    try:
        i=int(input("Enter an index: "))
        a=list[i]
        return a
    
    except:
        a="some error occured"
        return a

    print("very imp lines of code")

result=finding_a_value_from_list(list1)
print(result)

'''Now we all know that once the function returns with some value, the code written below it in the function 
defination doesn't gets executed'''

'''But if you want to do something like that , 'finally keyword' is the solution.'''
#Case2: Using finally keyword
list1=[1,2,4,8,16,32]

def finding_a_value_from_list(list):
    try:
        i=int(input("Enter an index: "))
        a=list[i]
        return a
    
    except:
        a="some error occured"
        return a

    finally:
        print("very imp lines of code") #This will be executed even before the return statement is executed

result=finding_a_value_from_list(list1)
print(result)


'''Now there are many cases in execution of finally. let us explore them one by one'''
#(I)-If exception occurs ,it is handeled by except:

def divide(x, y):
    try:
        result = x / y
        # print("result is", result)
    except ZeroDivisionError:
        print("division by zero!")
    else:
        print("result is", result)
    finally:
        print("executing finally clause")

divide(2, 1)