from array import *
x = [23,3323,5,67,567,899,56,67]
a=array('i',x)
min = a[0]

for i in range(0,len(a)):
    if min>a[i]:
        min=a[i]
print("Minimum value is",min)