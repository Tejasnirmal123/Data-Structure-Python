def binarySearch(list, target):
    s = 0
    e = len(list)
    while s <= e:
        mid = (s+e) // 2
        
        if list[mid] == target:
            print(f"Element found at index {mid}")

        if mid < target:
            s = mid + 1
        else:
            e = mid - 1

binarySearch([1,2,3,4,5,6,7,8], 2)


#BINARY SEARCH WITH RECURSION
# list = [1,2,3,4,5,6,7,8]
# s = 0
# e = len(list)-1

# def binarySearch(s, e, list, target):

   
#     if s >= e:
#         return -1
    
#     mid = (s+e) // 2
        
#     if list[mid] == target:
#         print(f"Element found at index {mid}")

#     if mid < target:
#         binarySearch(mid+1, e, list, target)
#     else:
#         binarySearch(s, mid-1, list, target)

# binarySearch(s,e,list,6)




