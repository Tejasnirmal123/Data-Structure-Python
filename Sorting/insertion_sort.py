list = [6,5,3,7,2,5,9,10,6]

def insertionSort(list):
    for i in range(1, len(list)):
        temp = list[i]
        j = i-1
        while list[j] > temp and j>=0:
            list[j+1] = list[j]
            j = j-1

        list[j+1] = temp 


        

insertionSort(list)
print(list)
