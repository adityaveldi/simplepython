x=[[1,2,3],
   [4,5,6],
   [7,8,9]]

y=[[1,2,3],
   [4,5,6],
   [7,8,9]]
print(x)
print(x[0])
result=[[0,0,0],[0,0,0],[0,0,0]]
if((len(x)==len(y)) and (len(x[0])==len(y[0]))):
   for i in range(len(x)):
      for j in range(len(x[0])):
         result[i][j]=x[i][j]+y[i][j]

print(result)