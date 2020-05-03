import java.util.*; 
  
class MaximumSubArray { 
    static List<Object> maxCrossingSum(int array[], int low, int mid, int high)
    { 
        int l_sum = Integer.MIN_VALUE; //- infinity
        int sum = 0; 
        int max_lindex=0;
        for (int i = mid; i >= low; i--) 
        { 
            sum = sum + array[i]; 
            if (sum > l_sum){ 
              l_sum = sum;
              max_lindex = i;
            }

        } 
        int r_sum = Integer.MIN_VALUE; 
        sum = 0; 
        int max_rindex=0;
        for (int i = mid + 1; i <= high; i++) 
        { 
            sum = sum + array[i]; 
            if (sum > r_sum){ 
              r_sum = sum; 
              max_rindex = i;
            }
        } 
        return Arrays.asList(max_lindex,max_rindex,l_sum + r_sum); 
    } 
  

    static List<Object> maxSubArraySum(int array[], int low,int high) 
    { 
      System.out.print(Arrays.toString(array));
      if (low == high) 
          return Arrays.asList(low, high, array[low]); 
      else{
        int mid = (low + high)/2; 
        List<Object> ll = maxSubArraySum(array, low, mid);
        List<Object> lr = maxSubArraySum(array, mid+1, high);
        List<Object> lc = maxCrossingSum(array, low, mid, high);
        int leftlow = (Integer) ll.get(0);
        int lefthigh =  (Integer) ll.get(1);
        int leftsum = (Integer) ll.get(2);
        int rightlow = (Integer) lr.get(0);
        int righthigh = (Integer) lr.get(1);
        int rightsum = (Integer) lr.get(2);
        int crosslow = (Integer) lc.get(0);
        int crosshigh = (Integer) lc.get(1);
        int crosssum = (Integer) lc.get(2);
        if ((leftsum >= rightsum)&& (leftsum>= crosssum)){
          return Arrays.asList(leftlow,lefthigh,leftsum);
          }
        else if((rightsum >= leftsum)&& (rightsum>= crosssum))
          return Arrays.asList(rightlow,righthigh,rightsum);
        else
          return Arrays.asList(crosslow,crosshigh,crosssum);
      } 
    }
  
    public static void main(String[] args) 
    { 
    int arr[] = {2, 3, 4, 5, 7}; 
    int n = arr.length; 
    List<Object> array = maxSubArraySum(arr, 0, n-1); 
      
    System.out.println("[low, high, sum]= "+  array); 
    } 
} 