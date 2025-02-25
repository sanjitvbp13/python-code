#write a program for finding NEXT GREATER element from in array.
size=int(input("Enter the size"))
list=[]
for i in range(0,size):
    list.append(int(input("Enter the element:")))
result = [-1]*size
for i in range(0,size):
    for j in range(i+1,size):
        if(list[j]>list[i]):
            result[i]=list[j]
            break
print(result)