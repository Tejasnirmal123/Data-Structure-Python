from array import *


arr = [1,4,5,6,7,8]

x = int(input("Enter number to search"))

for i in range(len(arr)):
    if arr[i] == x:
        print('your item is found at index number',i)
        break
else:
    print("your item is not found in this array")