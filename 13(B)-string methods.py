#6) center() -you can displace your string to the center and can even make use 
             # special characters 
str1="Papu can't dance saala" #length of str1 is 22
str2=str1.center(40) #***(A)HERE 40=22(string)+9(spaces-left)+9(spaces-right)
                     #***(B)Also this 40 is the length of the new string
                     #***(C)Note-White spaces are also considered while counting
                     #string length
str3="         Papu can't dance saala         " # the output of str2 and str3
                                                # will be the same   

str4=str1.center(40,"@") #All the above things can be easily understood using 
                         #str4
print(str1)
print(str2)
print(str3)
print(str4)
print(len(str1))
print(len(str2),len(str4))

#7)a) endswith() - will tell you wheter your string ends with the given set of characters or not 
               # for yes output = True , for no = False i.e boolean
a="yug ko research intership mili!!!"
print(a.endswith("!!!"))                 

#Note - We can carry out the same operation for a part of the given string
      # consider the nomenclature of slicing
      # first digit = index of the first character 
      # 'second digit-1' = index of the last character
a="yug ko research intership mili!!!" #Note-you can rewrite the same string in python any no 
                                      #     any no of times
print(a.endswith("h",4,15))

#7)b) starswith() - similar concept as of 8)a)
str1="yug ko sadbudhi do"
print(str1.startswith("yug"))
print(str1.startswith("sad",7,15))

#8) count() - counts the occurrence of a set of characters in a string
b="Har Har Mahadev"
print(b.count("Har"))
c="abracadabra" 
print(c.count("a"))

#9) find() - finds the first appearance of set of characters and gives it's index
            # and if the set of characters is not found then it gives '-1'
c="abracadabra"
print(c.find("a"))
d="hello hello can you hear me, can you see me"
print(d.find("can"))
print(d.find("cancel"))
str_is = "He's a strong guy.But he is polite." #Note - we know that in english he's 
                                                      #means he is but python don't 
                                                      #know english. so it finds the
                                                      #next is.
print(str_is.find("is"))

#10) index() - finds the first appearance of set of characters and gives it's index
             # and if the set of characters is not found then it gives error
d="hello hello can you hear me, can you see me"
print(d.index("can"))
# print(d.index("cancel")) #so if you are sure that you will definitely find the substring 
                           #in the given string then only use index(),otherwise use find  








