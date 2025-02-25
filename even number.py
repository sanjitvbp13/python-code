#1
#2 2
#4 4 4
#8 8 8 8
#16 16 16 16

n=1
for i in range(0,5):
  for j in range(0,i+1):
    print(n,end=" ")
  n=n*2
  print()