a = [1,4,3,2,30,8,9,20,10]

for i in range (len(a)):
    for j in range (i+1,len(a)):
        if a[i]>a[j]:
            a[i],a[j]=a[j],a[i]
print(a)






