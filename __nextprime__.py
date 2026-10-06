import __isprime__
integer=int(input("enter a number"))


def next_prime(num):
    while num>=2:
        num=num+1
        check=__isprime__.is_prime(num)
        if check==True:
            return num
            break
        else:
            pass

a=next_prime(integer)
print(a)
