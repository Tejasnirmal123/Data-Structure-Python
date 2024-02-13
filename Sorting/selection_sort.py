list = [1,5,3,7,2,5,9,10,6]

def selectionSort(list):
    for i in range(len(list)):
        
        minindex = i 
        for j in range(i+1, len(list)):
            if list[j] < list[minindex]:
                
                minindex = j
        temp = list[i]
        list[i] = list[minindex]
        list[minindex] = temp

selectionSort(list)
print(list)

