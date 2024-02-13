n = 5

for i in range(n):
    for j in range(i):
        print("*", end="")
    print()

# another method, we can add condition in if block
for i in range(1, 5):
    for j in range(1, 5):
        if j<=i:
            print("*",end='')
        else:
            print(" ",end='')
    print()

print()


for i in range(i):
    for j in range(n-i):
        print("*", end="")
    print()
    