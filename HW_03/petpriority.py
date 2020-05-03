from pet import *
class PetPriority(object): 
    def __init__(self, data, size): 
        self.arr = data
        self.size = size

x = -1 
heap = [0] * 1000 
sorted_list = []
class Sorting(PetPriority):
  def __init__(self, data, size): 
      PetPriority.__init__(self, data, size) 
 
  def heapForm(self, k): 
    global x; 
    x += 1; 
    heap[x] = k; 
    child = x; 
    index = x // 2; 
    while (index >= 0): 
        if (heap[index].name > heap[child].name): 
            tmp = heap[index]; 
            heap[index] = heap[child]; 
            heap[child] = tmp; 
            child = index; 
            index = index // 2; 
  
        else: 
            break;  
  def heapSort(self): 
    global x; 
    while (x >= 0): 
      k = heap[0]; 
      sorted_list.append(k)
      heap[0] = heap[x]; 
      x = x - 1; 
      tmp = -1; 
      index = 0; 
      length = x; 
      left1 = 1; 
      right1 = left1 + 1; 
      while (left1 <= length): 
        if (heap[index].name <= heap[left1].name and 
            heap[index].name <= heap[right1].name): 
            break; 
        else: 
          if (heap[left1].name < heap[right1].name): 
              tmp = heap[index]; 
              heap[index] = heap[left1]; 
              heap[left1] = tmp; 
              index = left1; 
          else: 
              tmp = heap[index]; 
              heap[index] = heap[right1]; 
              heap[right1] = tmp; 
              index = right1; 
          left1 = 2 * left1; 
          right1 = left1 + 1; 

  def sort_form(self,arr, size):
    for i in range(size): 
        self.heapForm(arr[i]) 
    self.heapSort() 

  def sort_temp(self):
    left= 0
    cat =[]
    dog = []
    for items in self.arr:
      if(isinstance(items,Cat)):
        cat.append(items)
        left+=1
      elif (isinstance(items,Dog)):
        dog.append(items)
      else:
        pass
    n = self.size
    self.sort_form(cat, left)
    self.sort_form(dog, n-left)
    return(sorted_list)
