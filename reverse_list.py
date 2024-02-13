
list = [1,2,3,4,5,6]
n = len(list)

s = 0
e = n-1

# while s<=e:
#     list[s], list[e] = list[e], list[s]

#     s= s+1
#     e = e-1

def reverse(s, e, list):
    if s>e:
        return
    
    list[s], list[e] = list[e], list[s]
    reverse(s+1,e-1,list)

reverse(s,e,list)
print(list)