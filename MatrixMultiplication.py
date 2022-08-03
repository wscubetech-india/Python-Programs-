A = [[1,2,3],
     [4,5,6],
     [7,8,9]]
B = [[1,2,1,1],
     [4,2,1,2],
     [6,3,4,1]]
result = [[0,0,0,0],
          [0,0,0,0],
          [0,0,0,0]]
for i in range (len(A)):
    for j in range (len(B[0])):
        for k in range (len(B)):
            result[i][j] += A[i][k] * B[k][j]

for i in result:
    print (i)


