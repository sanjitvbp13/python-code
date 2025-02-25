#1
#3 3 
#5 5 5
#7 7 7 7
#9 9 9 9 9

n=1
for i in range(0,5):
  for j in range(0,i+1):
    print(n,end=" ")
  n=n+2
  print()