def Shellsort(arr):
    size = len(arr) 
    gap = size//2
    while gap > 0: 
        for i in range(gap,size): 
            x = arr[i] 
            j = i 
            while  j >= gap and arr[j-gap] >x: 
                arr[j] = arr[j-gap] 
                j -= gap 
            arr[j] = x  
        gap //= 2
    return arr


array = list(map(int, input("Enter an array:\n ").split()))
print(array)  
sortedArray = Shellsort(array) 
print ("Array after sorting: \n") 
print(sortedArray)