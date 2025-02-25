#program to chrck whether a number is even or odd without modilas(%) operator.
#method_2
def is_even(n):
    if n & 1==1:
        return  False
    else:
        return True
print(is_even(14))  
print(is_even(17))  