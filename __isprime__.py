#Code to check whether the number is prime

# num1=int(input("enter a number"))

def is_prime(num):
    a=True

    if num<2:
        a=False
        return a

    elif num==2:
        pass
        return a

    else:
        for i in range(2,num):
            remainder=num%i
            if remainder==0:
                a=False
                break
            else:
                pass
        return a

# print(is_prime(num1))