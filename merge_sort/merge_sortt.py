arr = [1,4,5,6,7,89,45,23,22,56]

def merge_sort(arr):
    if len(arr) <= 1:
        return 
    
    mid = len(arr) // 2
    left = arr[:mid]
    right = arr[mid:]

    merge_sort(left)
    merge_sort(right)

    merge_two_sorted_lists(left, right, arr)

def merge_two_sorted_lists(a,b, arr):
    len_a = len(a)
    len_b = len(b)
    i = j = k = 0

    while i < len_a and j < len_b:
        if a[i] <= b[j]:
            arr[k] = a[i]
            i = i + 1
            
        else:
            arr[k] = b[j]
            j = j + 1
        k = k + 1

    while i < len_a:
        arr[k] = a[i]
        i = i + 1
        k = k + 1

    while j < len_b:
        arr[k] = b[j]
        j = j + 1
        k = k + 1


merge_sort(arr)
print(arr)
