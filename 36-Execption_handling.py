#Exception handling is done so as to let the excecution of the code to be continued , because if error occurs then
#interpretation is stopped at that line itself and an exception is thrown.

#Ex-1:
a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")
try:
  for i in range(1, 11):
    print(f"{int(a)} X {i} = {int(a)*i}")
except:
  print("Invalid  Input!")

print("Some imp lines of code")#...(If the exception wasn't handled ,these lines of code wouldn't have been executed)
print("End of program")


#Ex-2: You can also access the statement (given by python interpreter) of the exception occured using 'as' to 
#      create an instance of class Exception(concept is not perfectly clear)
a = input("Enter the number: ")
print(f"Multiplication table of {a} is: ")
try:
  for i in range(1, 11):
    print(f"{int(a)} X {i} = {int(a)*i}")

except Exception as e: #Note here the syntax is important
  print(e)

print("Some imp lines of code")
print("End of program")


#You can also handle specific types of errors
#Ex-1:
try:
    num = int(input("Enter an integer: "))

except ValueError:
    print("Number entered is not an integer.")


#Ex-2:
try:
    num = int(input("Enter an integer: "))
    a=[3,6]
    print(a[num])

except ValueError:
    print("Number entered is not an integer.")

except IndexError:
    print("Given list is small to access the given index")


