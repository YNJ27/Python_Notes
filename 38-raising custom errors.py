# It is generally used to stop the execution of code intentionally at some specific line for some reasons 
# like if user gives unexcepted inputs or so. 

# For ex: Mummy wanted you to give samosas to your Mausi, But she by mistakely gave you a bag of vegetables.
#        Now you saw this when you were on the way, so you would definetiy like to stop at that point and
#        would not like to go ahead. 

#Ex:
num1 = int(input("Enter a no between 5 and 9: "))
if ((num1 < 5) or (num1 > 9)):
    raise ValueError("Value should be between 5 and 9")



# Create a program which will ask for a number from the user and will raise an error if the number is
#1) less than 5 or greater than 9
#2) it is any string other than 'quit'

a = input("Enter a number between 5 and 9: ")

if (a == "quit"):
  print("ohk")
elif (int(a) < 5 or int(a) > 9):
  raise ValueError("The number should be between 5 and 9")


#We can also create user defined errors for special reasons using the concept of class