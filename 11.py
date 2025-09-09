x=[[2,3,4],
   [5,6,8],
    [6,7,3]]

y=[[8,9,7],
    [3,4,5],
    [7,6,8]]
add=[[x[i][j]+y[i][j]
      for j in range (len (x[0]))]
      for i in range (len (x))]
print ("addition of matrix:")
for row in add:
    print(row)
