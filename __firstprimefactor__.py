import __isprime__
import __nextprime__

def first_prime_factor(num):
    a=2
    remainder=num%a
    if remainder==0:
        return a
    else:
        while remainder!=0:
            a=__nextprime__.next_prime(a)
            remainder=num%a
        return a


        