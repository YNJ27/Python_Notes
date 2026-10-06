#problem1 - without using replace , replace h by k
string = input()
new_str = ""
for i in range(len(string)):
    if string[i] == "h" :
        new_str = new_str + "k"
    else:
        new_str = new_str + string[i]
print(new_str)


#similar problem using (inbuilt) slicing 
def mutate_string(string, position, character):
    str1=string[:position]
    str2=string[position+1:]
    str_new=str1+character+str2
    return str_new 

string1=input("Enter your string: ")
position1=int(input("Enter the index of the character you want to change: "))
character1=input("Enter the replacement you want for that character: ")

print(mutate_string(string1, position1, character1))
