# search-in-2d-matrix
def search(mat,target,n):
  i=0
  j=n-1
  while i<n and j>=0:
    if mat[i][j]==target:
      return True
    if mat[i][j]>target:
      j-=1
    else:
      i+=1
  return False
