
class Mergesort {
  public static void main(String[] args) {
        int a[] = {5, 2, 4, 7, 1, 3, 2, 6}; 
  
        System.out.println("Given Array"); 
        printArray(a); 
  
        Main ob = new Main(); 
        ob.Mergesort(a, 0, a.length-1); 
  
        System.out.println("\nSorted array"); 
        printArray(a); 
  }
void merge(int a[], int p, int q, int r) //(int arr[], int l, int m, intr)
  { 
    int i=0; 
    int j=p;
    int k=q+1; 
    int size = r - p + 1; 
    int b[] = new int[size];
    while (j<=q && k<=r) 
    {
      if (a[j]<=a[k]) 
        {
        b[i]=a[j];
        i++;
        j++;
        }
      else 
      {
        b[i]=a[k];
        i++;
        k++;
      }
    }
    while (j<=q)
    {
      b[i]=a[j];
      i++;
      j++;
    }
    while (k<=r) 
    {
      b[i]=a[k];
      i++;
      k++;
    }
    for (int z = p; z<=r; z++){
       a[z]=b[z-p];
    }
     
  } 

  void Mergesort(int a[], int p, int r)
  { 
    if (p < r) 
    { 
      int q = (p+r)/2; 
      Mergesort(a, p, q); 
      Mergesort(a , q+1, r); 
      merge(a, p, q, r); 
    } 
  } 
  static void printArray(int arr[]) 
  { 
    int n = arr.length; 
    for (int i=0; i<n; ++i) 
    System.out.print(arr[i] + " "); 
    System.out.println(); 
  } 
}
