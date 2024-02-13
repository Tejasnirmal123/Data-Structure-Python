from array import *

x = [23,78,65,4,3,12,]
a = array('i',x)
max=a[0]


for i in range (0,len(a)):
    if a[i]>max:
        max = a[i]
print("Maximum Value Is",max)