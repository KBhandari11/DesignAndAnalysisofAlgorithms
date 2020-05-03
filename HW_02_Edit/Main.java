//Kushal Bhandari


import java.util.Arrays;
import java.util.Scanner;
import java.lang.Math;

class Main
{
    public static int[][] Main(int[][] X, int[][] Y)
    {
    	return  matrixDivideConquer(X, Y, 0, 0, 0,0, X.length);
	}


	public static int[][] matrixDivideConquer(int[][] X, int[][] Y, int rowX, int colX, int rowY, int colY, int size)
	{
	    int[][] Z = new int[size][size];

	    if(size==1)
	        Z[0][0]= X[rowX][colX] * Y[rowY][colY];

	    else
	    {
	        int newSize= size/2;
	        
	        sumMatrix(Z,
	            		matrixDivideConquer(X, Y, rowX, colX, rowY, colY, newSize),
	            		matrixDivideConquer(X, Y, rowX, colX+newSize, rowY+ newSize, colY, newSize),
	        			0, 0);

	        sumMatrix(Z,
	            		matrixDivideConquer(X, Y, rowX, colX, rowY, colY + newSize, newSize),
	            		matrixDivideConquer(X, Y, rowX, colX+newSize, rowY+ newSize, colY+newSize, newSize),
	        			0, newSize);

	        sumMatrix(Z,
	            		matrixDivideConquer(X, Y, rowX+ newSize, colX, rowY, colY, newSize),
	            		matrixDivideConquer(X, Y, rowX+ newSize, colX+newSize, rowY+ newSize, colY, newSize),
	        			newSize, 0);

	        sumMatrix(Z, 
	            		matrixDivideConquer(X, Y, rowX+ newSize, colX, rowY, colY+newSize, newSize),
	            		matrixDivideConquer(X, Y, rowX+ newSize, colX+newSize, rowY+ newSize, colY+newSize, newSize),
	        			newSize, newSize);
	    }

	    return Z;
	}


	private static void sumMatrix(int[][] Z, int[][]X, int[][]Y,int rowC, int colC)
	{
	    int n=X.length;
	    for(int i=0; i<n; i++)
	    {
	        for(int j=0; j<n; j++)  
	            Z[i+rowC][j+colC] = X[i][j] + Y[i][j];
	    }

	}

	public static void main(String[] args) 
	{
	  int X[][] = { {1, 2, 3, 4}, 
                  {5, 6, 7, 8}, 
                  {9, 10, 11, 12},
                  {13, 14, 15, 16}}; 
   
    int Y[][] = { {1, 2, 3, 4}, 
                  {5, 6, 7, 8}, 
                  {9, 10, 11, 12},
                  {13, 14, 15, 16}}; 
    
    System.out.println("\nArray X");
    for(int[] row : X)
	        System.out.println(Arrays.toString(row));
    System.out.println("\nArray Y");
    for(int[] row : Y)
	        System.out.println(Arrays.toString(row));
	    // Recursive Square Matrix Multiplication
	    int[][] Z = Main(X, Y);


	    System.out.println("\nArray Z = X x Y:");
	    for(int[] row : Z)
	        System.out.println(Arrays.toString(row));
	}
}
