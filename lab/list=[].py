list=[]
s = int(input("Enter the size of list:"))
for i in range (0, s):
    a = int(input("enter the number"))
    list.append(a)
n = int(input("Enter the diserd number:"))
if n in list:
     print("Yes")
else:
     print("No")
