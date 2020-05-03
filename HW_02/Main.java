//Kushal R. Bhandari
class Main {
    public static int MAX = 100; 

    public static int x = 0, y = 0, z = 0; 
      
    static void multiplyMatrixRec(int A[][], int B[][],int Multi[][]) 
    { 
        if (x >= A.length) 
            return; 
           if (y < B[0].length) 
        { 
            if (z < A[0].length) 
            { 
                Multi[x][y] += A[x][z] * B[z][y]; 
                z++; 
   
                multiplyMatrixRec( A, B, Multi); 
            } 
            z = 0; 
            y++; 
            multiplyMatrixRec(A, B, Multi); 
        } 
        y = 0; 
        x++; 
        multiplyMatrixRec(A, B, Multi); 
    } 
   
    static void multiplyMatrix(int A[][],int B[][]) 
    { 

   
        int[][] Multi = new int[MAX][MAX]; 
   
        multiplyMatrixRec(A, B, Multi); 
   
        for (int i = 0; i < A.length; i++) 
        { 
            for (int j = 0; j < B[0].length; j++) 
                System.out.print(Multi[i][j]+" "); 
   
            System.out.println(); 
        } 
    } 
      
    // driver program 
    public static void main (String[] args)  
    { 
        int A[][] = { {1, 2, 3, 4}, 
                      {5, 6, 7, 8}, 
                      {9, 10, 11, 12},
                      {13, 14, 15, 16}}; 
   
        int B[][] = { {1, 2, 3, 4}, 
                      {5, 6, 7, 8}, 
                      {9, 10, 11, 12},
                      {13, 14, 15, 16}}; 
   
        multiplyMatrix(A, B); 
    } 
  
}