sum1=0
sum2=0
matrix=[]
for i in range(0,3):
    for j  in range(0,3):
        if i ==  j:
            sum1=sum1+matrix[i][j]
        if i+j==len(matrix)-1:
            sum2 = sum2 + matrix[i] [j]
print(Sum1)
print(sum2)