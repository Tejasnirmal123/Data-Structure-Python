from array import *
sum = 0
arr = []

value = int(input("Enter Size Of Array"))

for i in range(value):
  
    x = int(input("Enter The Next Number"))
    
   
    #arr[i] = x
    arr.append(x)
    sum = sum + arr[i]
    
print(sum)








# integer_list = [5, 10, 15, 20, 25, 30, 35, 40, 45]

# for n in integer_list:
#     index = 0
#     index += n
#     print (index)



