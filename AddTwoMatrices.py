A = [[1,2,3],
     [7,8,9],
     [4,5,6]]
B = [[7,8,9],
     [12,34,6],
     [1,2,3]]
result =[[0,0,0],
         [0,0,0],
         [0,0,0]]

for i in range (len(A)):
    for j in range (len(A[0])):
        result[i][j] =A[i][j] + B[i][j]

print (result)

for i in result:
    print (i)