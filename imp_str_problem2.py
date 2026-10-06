#problem2 - without using any string methods print 123....n if input is an integer n
n = int(input())
str1=""
for i in range (1,n+1):
        str2=str(i)
        str1=str1+str2
print(str1)
