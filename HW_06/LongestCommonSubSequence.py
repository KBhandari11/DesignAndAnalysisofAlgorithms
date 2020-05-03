
X, Y = input("Enter two different text for subsequencing: \n (Example:LONGESTCOMMON LOMON)   \n").split()


memo =[[-1 for i in range(len(Y)+1)] for j in range(len(X)+1)]


def LCS_Length(X, Y):
  length = SubProblem(len(X), len(Y))
  value = SubProblem_String(len(X), len(Y))
  return length, value

  

def SubProblem(i, j):
  if(i==0 or j==0):
    memo[i][j]=0
  elif (X[i-1]==Y[j-1]):
    memo[i][j] = 1 + SubProblem(i-1,j-1)
  else:
    memo[i][j]= max(SubProblem(i-1, j), SubProblem(i,j-1))
  return memo[i][j]

def SubProblem_String(i, j):
  if(i==0 or j==0):
    return ""
  elif (X[i-1]==Y[j-1]):
    return SubProblem_String(i-1,j-1) + X[i-1]
  else:
    return max(SubProblem_String(i-1, j), SubProblem_String(i,j-1))



length, value = LCS_Length(X, Y)
print("The Length is: ",length)
print("The Sequence is: ",value)

