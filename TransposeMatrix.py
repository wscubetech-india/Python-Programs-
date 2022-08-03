#Solution 1 Using for loop
#
# A = [[1,2,3],
#      [4,5,6]]
# T = [[0,0],
#      [0,0],
#      [0,0]]
# for i in range (len(A)):
#     for j in range (len(A[0])):
#         T[j][i]=A[i][j]
# for i in T:
#     print (i)

#Solution 2 Using List Comprehension
A = [[1,2,3],
     [4,5,6]]

T = [[A[j][i] for j in range (len(A))] for i in range (len(A[0]))]

for i in T:
    print (i)

