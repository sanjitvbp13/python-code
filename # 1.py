#      1 
#    1 2#
#  1 2 3
#1 2 3 4
#1 2 3 4 5

n=5
for i in range(0,5):
 for k in range(4,i,-1):
    print(" ",end="")
    for j in range(0,i+1):
    print(j+1,end="")
  print()

#    1 
#   1 2 
 # 1 2 3 
# 1 2 3 4 
#1 2 3 4 5 
#n=6
#for i in range(0,5):
 # for k in range(4,i,-1):
 #   print(" ",end="")
 # for j in range(0,i+1):
     print(j+1,end=" ")
 # print()