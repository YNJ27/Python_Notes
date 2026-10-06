num1=int(input("Enter a number: "))
import __isprime__
import __nextprime__
import __firstprimefactor__
def prime_factors(num):
    list1=[1]
    factor=__firstprimefactor__.first_prime_factor(num)
    while num>1:
        while num%factor==0:
            list1.append(factor)
            num/=factor
        factor=__nextprime__.next_prime(factor)
    return list1

prime_Factors=prime_factors(num1)
print("The prime factors of given number are:",prime_Factors)