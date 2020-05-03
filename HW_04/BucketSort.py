def partition(arr,low,high): 
  i = ( low-1 )        
  pivot = arr[high]   
  for j in range(low , high): 
    if   arr[j] < pivot: 
      i = i+1 
      arr[i],arr[j] = arr[j],arr[i] 
  arr[i+1],arr[high] = arr[high],arr[i+1] 
  return ( i+1 ) 
  
def quickSort(arr,low,high): 
    if low < high: 
        pi = partition(arr,low,high) 
        quickSort(arr, low, pi-1) 
        quickSort(arr, pi+1, high) 
    return arr

def bucketSort(x): 
    sortedArr = [] 
    SIZE = 10 
    for i in range(SIZE): 
        sortedArr.append([]) 
          
    for j in x: 
        index_b = int(SIZE * j)  
        sortedArr[index_b].append(j) 
      
    for i in range(SIZE): 
        n = len(sortedArr[i]) 
        sortedArr[i] =quickSort(sortedArr[i],0,n-1)
          
    k = 0
    for i in range(SIZE): 
        for j in range(len(sortedArr[i])): 
            x[k] = sortedArr[i][j] 
            k += 1
    return x 
  

array = [0.897, 0.565, 0.656, 
     0.12344, 0.61665, 0.352434,0.835197, 0.54625, 0.6526, 
     0.13234, 0.6675, 0.342434,0.57897, 0.55625, 0.6256, 
     0.11234, 0.6265, 0.34734,0.8897, 0.5465, 0.6156, 
     0.122134, 0.6365, 0.36434,0.9897, 0.52365, 0.6856, 
     0.12234, 0.6265, 0.343454,0.8987, 0.2565, 0.66596, 
     0.122334, 0.6365, 0.533434,0.7897, 0.56655, 0.76856, 
     0.12234, 0.6615, 0.34434]  
print("Sorted Array is") 
print(bucketSort(array)) 
  