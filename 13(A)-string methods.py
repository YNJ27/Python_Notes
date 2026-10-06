#***STRINGS ARE IMMUTABLE***

#STRING METHODS
#1) upper() - all the characters are converted into uppercase
a="Yug"
print(a.upper()) #Note-the output of this command is a new string with
                 #     uppercase. it is not the same string

#2) lower()      
b=a.lower()
print(b)



#3)a) rstrip() - removes all the defined characters from the end
             # IT CAN'T REMOVE THE LEADING ONES
c="Harry!!!!!!!!"
print(c)
print(c.rstrip("!"))

d="******yug******"
print(d.rstrip("*"))

#3)b) lstrip - removes all the defined characters from the starting 
            #  of the string only
str_4="******yug******"
print(str_4.rstrip("*"))

#3)c) strip - removes all the defined characters both from the starting and 
             #ending of the string
str_1="!!!!!Harry!!!!!"
print(str_1.strip("!"))

str_2="  yug    "
print(str_2.strip()) #by default all the variants of strip method removes 
                     #whitespaces

str_3="  yu  g   "
print(str_3.strip()) #it can't remove anything from middle

#4) replace() - replaces all occurrences of a string with another string
e="om#####om#####om"
print(e)
f=e.replace("om","yug")
print(f)

#5)a) split() - splits the string and creates a list with entries as the
            # splitted characters
g="yug~~~om~~~dev"
h=g.split("~~~") 
print(h) #It will also remove the defined characters 

i="***YUG ***OM ***DEV"
print(i.split(" "))

#b)join() - joins the items of a list/tuple/dictionary(only keys) to form a string with defined 
           #seperator
           #Note : syntax is different, so be careful while using

new_str=" ".join(h) #Here anything defined inside the double quotes 
                    #is considered as the seperator 
print(new_str)

new_str2="~~~".join(h)
print(new_str2)        #it will give you a string equivalent to 'g'.

string = "Om Yug Dev"
temp_list = string.split()
print(temp_list)

reconstructed_string = " ".join(temp_list)
print(reconstructed_string)
print(type(reconstructed_string)) #it will give you a string equivalent to 'string'.