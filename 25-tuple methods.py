#Tuple methods 
# we know that tuples are immutable , but still if you want to make changes to it ,typecast it to list first and 
# then make changes to it, at the end typecast it back to tuple.But note that the former and the later tuples 
# will not be the same, even though you give them the same name. 

tup1=(1,3,"yug","dev")
print(id(tup1))            

temp=list(tup1)
temp.remove("dev")
temp.insert(0,"om")

tup1=tuple(temp)
print(id(tup1))
print(tup1)

#concatenation of tuples - this is allowed because we are actually creating a new tuple without altering the 
#individual tuples
tup1=(100,200)
tup2=(300,400,500)
tup3=tup1+tup2 
print(tup3)

#1) count() 
tup1=(1,2,3,1,4,"dev")
print(tup1.count(1))

#2)index()
print(tup1.index(1))
# also you can find the index of the further occurences using slicing

