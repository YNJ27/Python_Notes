# Using recursion:
def fibbonacci(num):
    if num==1:
        a=0
        return a

    elif num==2:
        a=1
        return a

    else:
        return (fibbonacci(num-1)+fibbonacci(num-2)) 

num1=int(input("Enter the position of the number you want from fibbonacci series: "))
print(fibbonacci(num1))