n = 6

for i in range(n):
    for j in range(i):
        print(j+1, end="")
    print()

print()

for i in range(n):
    for j in range(n-i):
        print(j+1, end="")
    print()

print()


for i in range(n):
    for j in range(i):
        print(i, end="")
    print()