from array import *


x = [1,2,4]
y = [4,5,6]

a = array('i',x)
b = array('i',y)

for i in range(0,len(a)):
    if a[i]>a[i+1]:
        a[i]=a[i+1]

print(a[i])


    

