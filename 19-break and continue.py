#break 
#ex-1:
for i in range(1,11):
    if i==7:
        break        #it will get out of the loop (and no line of the loop
                     #below it will be excecuted for the given iteration)
        print("Sir-Don't watch match,study for exam")   
                                                             
    else:
        print(i)
print("Me to match hi dekhoonga kyuki me MAHI ka fan hoon")

#ex-2: little change
for i in range(1,11):
    if i==7:
        print("Papa-abhi match dekhlo par,badme padhai bhi karna,exam hai na")
        break        #it will get out of the loop (and no line of the loop
                     #below it will be excecuted for the given iteration)
        print("Sir-Don't watch match,study for exam")   
                                                             
    else:
        print(i)
print("Ok Papa thodi der dekhne ke baad padhai karunga,because MAHI mar raha hai")

#continue
#ex-3
for i in range(1,11):
    if i==7:
        print("bhai me football nahi dekhta")
        continue      #it will get out of this iteration and here also no line below 
                      #will be executed. And will directly jump to the next iteration
        print("make some noise for CR7")
    else:
        print(i)

