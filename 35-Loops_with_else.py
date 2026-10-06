# As you have learned before, the else clause is used along with the if statement.
# Python allows the else keyword to be used with the for and while loops too. 
# The else block appears after the body of the loop.
# The statements in the else block will be executed after all iterations are completed.
'''MOST IMPORTANT - The program exits the loop only after the else block is executed.'''

#Ex-1 : Using while loop
i = 1
while i<6:
  print(i)
  i = i + 1

else:                      #....(Actually this else is a part of the loop.)
  print("Sorry no i") 


#Ex-2 : Using for loop
for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
else:
    print ("else block in loop")

print ("Out of loop")



#Most important concept - 
for x in range(5):
    print ("iteration no {} in for loop".format(x+1))
    if x==2:
        break
else:
    print ("else block in loop")

print ("Out of loop")

'''Now here as we broke the loop , else block will not be executed(This is because it is a part of the loop itself)













    # if i == 4:
  #   break      '''