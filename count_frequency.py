arr = [1,2,3,1,4,5,3,4,6,7,5]
print(arr)

d = {}
for i in arr:
    d[i] = d.get(i,0)+1
print(d)