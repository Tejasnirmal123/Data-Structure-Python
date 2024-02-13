a = [1,2,4,67,89,90]

b = [3,5,6,7,8,9,15,40,90]




def merge_two_sorted_lists(a,b):
    sorted_list = []
    len_a = len(a)
    len_b = len(b)
    i = j = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            sorted_list.append(a[i])
            i = i + 1
        else:
            sorted_list.append(b[j])
            j = j + 1

    while i < len_a:
        sorted_list.append(a[i])
        i = i + 1
    while j < len_b:
        sorted_list.append(b[j])
        j = j + 1
    
    
    return sorted_list

print(merge_two_sorted_lists(a, b))


