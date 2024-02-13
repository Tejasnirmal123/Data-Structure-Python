from array import *
temp = 0

a = [1,5,7,8,34,10,20]

for i in range ((len(a))):
    for j in range (i+1, len(a)):
        if a[i]<a[j]:
            temp = a[i]
            a[i]=a[j]
            a[j]=temp

print("second largest number is",a[1])


