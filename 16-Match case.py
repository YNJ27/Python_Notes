'''match cases - it compares the given value of variable with the cases,and
the first case which is matched is executed(though the further cases are 
matching or not.)'''
'''if no case is matched the default case is executed'''
#eg:
num=int(input("enter a number: "))
match num:
    case 22:
        print("it's my birth date")
    case 5:
        print("it's my mother's birth date")
    case 20:
        print("it's my father's birth date")
    case 4:        
        print("it's Dev's birth date")
    case 24: 
        print("it's Om's birth date")
    
    case _ if(num!=26):#default case1 
        print("it can't be Yashwant's birth date")
    case _ : #default case2
        print("""it is Yashwant's birthdate""")

'''note1: the basic syntax of default case is the same as that of the case 2
   note2: in the default cases also, the one matched first is executed,and 
   remaining cases are not'''

""" generally cases are used as 'if with ==' and default cases are used as
    else"""