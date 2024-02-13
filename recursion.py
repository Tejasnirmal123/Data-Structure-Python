# calculate sum of a number 
def find_sum(n):
    if n == 1:
        return 1
    return n + find_sum(n-1)

print (find_sum(4))


# find factorial of a number with recursion 
def fact(n):
    if n==0 or n==1:
        return 1
    return n * fact(n-1)

print(fact(5))



# fibonacci series with recursion
# 0 1 1 2 3 5 8
def fib(n):
    
    if n == 0 or n == 1:
        return n
    return fib(n-1) + fib(n-2)

fib(6)
for i in range(6):
    print(fib(i))
