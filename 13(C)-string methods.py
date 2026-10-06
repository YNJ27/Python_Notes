#11) isalnum() - if your string is made up only of A-Z,a-z,0-9 then it will give True, otherwise false.
               #Note- it is not comsulsary that it should be made of all the above sets 
               #it can be made of any of the above sets 
Alnum_Str="Golmaal3"
print(Alnum_Str.isalnum())
Num_Str="8754"
print(Num_Str.isalnum())
Not_atall_alnum="%#$*@"
print(Not_atall_alnum.isalnum()) #will give False
Sp_Chr_and_Alnum="Yug_Nitin_Jain"
print(Sp_Chr_and_Alnum.isalnum()) #will give False
Alnum_with_whitespaces="Om Sunil Jain"
print(Alnum_with_whitespaces.isalnum()) #***Note***-whitespaces are also not allowed
                                        #So will give False

#12) isalpha - Only A-Z, a-z (theory relates with isalnum)
Alpha="Aman"
print(Alpha.isalpha())
Alnum_Str="Golmaal3"
print(Alnum_Str.isalpha())
Alnum_with_whitespaces="Om Sunil Jain"
print(Alnum_with_whitespaces.isalpha()) #same reason as given in alnum()

#13) isower() - gives True if all characters in the string are in lowercase
               #otherwise false
Lower_Str="yug nitin jain"
print(Lower_Str.islower())
Lower_Str_with_numbers_and_Spcecial_characters="yug % nitin 5 jain"
print(Lower_Str_with_numbers_and_Spcecial_characters.islower()) #No problem with 
                                                                #with numbers and
                                                                #special characters

#14) isupper() - same as islower

#15) isprintable() - gives True if all the characters in the string are printable
printable_str="Yug ke paas acer hai"
print(printable_str.isprintable())
exceptional_str="Yug is \'king\'" # though ( \ ) is not printed it not gives false
print(exceptional_str)
print(exceptional_str.isprintable())
nonprintable_str="Yug was born in RTN\nHe currently lives in pune"
print(nonprintable_str.isprintable())
# there are also some other escape sequences like \v,\t,\r
#there is a problem in working of \v in vs.code

#16) isspace() - gives True if the string has only whitespaces and nothing else
                #otherwise gives false
Str_Only_Spaces="  "
Str_with_chrs_and_spaces="Yug Nitin Jain"
print(Str_Only_Spaces.isspace())
print(Str_with_chrs_and_spaces.isspace()) 

#17) istitle() - gives True if the first letter of each word in a string is capital
                #otherwise false
title_str="World Health Organisation" 
print(title_str.istitle())
title_str_with_nums_and_spc_chrs="5World @Health 8Organisation"
print(title_str_with_nums_and_spc_chrs.istitle())
#Note-it ignores numbers and special characters

#18) swapcase() - The swapcase() method changes the character casing of the string.
                 #Upper case are converted to lower case and lower case to upper case.
str_a="Python is a Interpreted Language" 
print(str_a.swapcase())

#19) title() - It capitalizes the first letter of the each word of the string
str_b = "he1s a strong guy.but he is polite."
print(str_b.title()) 
#search about ' and similar exceptions

#20) capitalize() - converts the first letter of the string to uppercase
                #  and all other letters to lowercase
heading="welcome tO My Code"  
print(heading.capitalize())          

heading2="Welcome To mY coDE"    
print(heading2.capitalize()) 

heading3="Welcome to my code"
print(heading3.capitalize()) #if the first letter is in uppercase and all
                            #all other letters are in lowercase there will 
                            #be no change

'''little deep knowledge of both capitalize() and title() is given on my vlog'''