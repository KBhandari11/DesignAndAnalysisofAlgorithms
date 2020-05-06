import numpy as np

def printing(X,name):
  X= np.around(X, decimals=2)
  n = np.shape(X)[0]
  L = np.zeros((n,n))
  U = np.zeros((n,n))
  for i in range(n):        
    L[i][i]= 1
  print("*****"+name+"*****"); 
  for i in range(n): 
      for j in range(n): 
          print(X[i][j], end = "\t\t");  
      print("");
def luDecomposition(mat):
    n = np.shape(mat)[1]
    lower = np.zeros((n,n))
    upper = np.zeros((n,n))
    for i in range(n):        
      lower[i][i]= 1
    for k in range(n):
        upper[k][k] = mat[k][k]
        for i in range(k+1,n):
            lower[i][k]= mat[i][k]/upper[k][k]
            upper[k][i]= mat[k][i]
        for i in range(k+1,n):
            for j in range(k+1,n):
                mat[i][j]= mat[i][j] - (lower[i][k]*upper[k][j])     
    return (lower, upper)
def lupDecomposition(mat):
    n = np.shape(mat)[0]
    L = np.zeros((n,n))
    U = np.zeros((n,n))
    pi =np.arange(n)
    for k in range(n):
      p =0 
      for i in range(k,n):
        if abs(mat[i][k]) > p :
          p =abs(mat[i][k])
          ki = i
      if p == 0:
        raise NameError("It is a Singular Matrix")
      temp = pi[k]
      pi[k] = pi[ki]
      pi[ki] = temp
      for i in range(n):
        temp = mat[k][i]
        mat[k][i] =mat[ki][i]
        mat[ki][i]= temp
      for i in range(k+1,n):
        mat[i][k] = mat[i][k]/mat[k][k]
        for j in range(k+1,n):
          mat[i][j]= mat[i][j] - (mat[i][k]*mat[k][j])
    for i in range(n):
      for j in range(n):
        if (i <= j):
          U[i][j] = mat[i][j]
        else: 
          L[i][j] = mat[i][j]
    return L, U, pi
def lupSolve(L,U,pi,b):
  n= np.shape(L)[1]
  x= np.ones(n)
  y= np.ones(n)
  for i in range(n):
    y[i] = b[pi[i]]- sum([L[i][j]*y[j] for j in range(n-1)])
  for i in range(n-1, -1, -1):
    x[i]=(y[i]-sum([U[i][j]*x[j] for j in range(i+1,n)]))/U[i][i]
  return x
'''

mat = [[2, 3, 1, 5], 
       [6, 13, 5, 19],
       [2, 19, 10, 23],
       [4, 10, 11,31]];  
L, U = luDecomposition(mat); 
printing(L," LU Decomposition L ")
printing(U, " LU Decomposition U ")

mat = [[2, 0, 2, 0.6], 
       [3, 3, 4, -2],
       [5, 5, 4, 2],
       [-1, -2, 3.4,-1]]; 
L, U, pi = lupDecomposition(mat)
printing(L," LU Decomposition L ")
printing(U, " LU Decomposition U ")
'''
mat=[[1,2,0],
    [3,4,4],
    [5,6,3]]
b=[3,7,8]
L, U, pi = lupDecomposition(mat)
printing(L," LU Decomposition L ")
printing(U, " LU Decomposition U ")
x = lupSolve(L,U,pi,b)
print(x)

'''
mat = [[-3, -1, -3], 
       [3, 2, 3],
       [2, 1, 2]]; 
L,U, pi = lupDecomposition(mat)
printing(P, " LUP Decomposition P ")
'''