#ques1
lst=[2,3,4,5,6]
lst1=[i*i*i for i in lst]   
print(lst)
print(lst1)

#ques2
prime=[x for x in range(2, 20)if all(x % y != 0 for y in range(2, x))]
print(prime)

#ques3
import sys
l = [n*2 for n in range(1000)] 
g = (n*2 for n in range(1000))
 
print(type(l))  
print(type(g))  
 
print(sys.getsizeof(l))  
print(sys.getsizeof(g))  
 
print(l[4])   
print(g[4])   
 
for v in l:
    pass
for v in g:
    pass

#ques4
celsius=[39.2,36.5,37.3,37.8]
fahren=list(map(lambda x:(x*1.8)+32,celsius))
print(fahren)

#ques5
lst=[2,3,4,5]
lst1=list(map(lambda x:x*x,lst))
print(lst)
print(lst1)


#ques6
def prime(number):
    if number>1:
        for i in range(2,number):
            if (number%i)==0:
                break
        else:
            return number
lst=[1,2,3,4,5,6,7,8,9,10]
primeno=list(filter(prime,lst))
print(primeno)

#ques7
from functools import *
lst=[2,3,6,7,8]
mul=reduce(lambda x,y:x*y,lst)
print(mul)
