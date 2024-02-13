from array import *
k=0
arr=[]
rows, cols = 5,5
for i in range(rows):
    
    for j in range(cols):
        if j<=1:
            arr[i][j]=k*j+1
            #arr[i][j].append(k*j+1)
    k=k+1

for i in range(rows):

    for j in range(cols):
        print(arr[i][j])
    print()

    

  