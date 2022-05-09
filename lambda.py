def even(n):
    return n%2==0

list1=[2,13,42,4,524,331,67,89,45,90]

list_even=list(filter(even,list1))
print(list1,list_even)

#print odd and even list
def even(n):
    return n%2==0

list1=[2,13,42,4,524,331,67,89,45,90]

list_even=list(filter(lambda x : x%2==0,list1))
list_odd=list(filter(lambda x : x%2!=0,list1))
print(list1)
print(list_even)
print(list_odd)

#har ek list k no ko 2 se multiply krna h..
#koi specific value ko nikalne k liye list m se  filter ka use kiya h
#m values ko extract kiya jata h
def even(n):
    return n%2==0

list1=[2,13,42,4,524,331,67,89,45,90]

list_even=list(filter(lambda x : x%2==0,list1))
list_odd=list(filter(lambda x : x%2!=0,list1))
print(list1)
print(list_even)
print(list_odd)
#map m values ko chng bhi krhe h 

list_even2=list(map(lambda x:x*2,list_even))
print(list_even2)

#sabhi elements ka sum nikalna even no ka jo hmne abhi jisko 2 se multiply kiya h
def even(n):
    return n%2==0
from functools import reduce#reduce ko import krne k liye
list1=[2,13,42,4,524,331,67,89,45,90]

list_even=list(filter(lambda x : x%2==0,list1))
list_odd=list(filter(lambda x : x%2!=0,list1))
print(list1)
print(list_even)
print(list_odd)

list_even2=list(map(lambda x:x*2,list_even))
print(list_even2)

sum=reduce(lambda x,y:x+y,list_even2)
print(sum)
