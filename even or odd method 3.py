#program to chrck whether a number is even or odd without modilas(%) operator.
#method_3
def is_even(n):
    if n^1==n-1:
        return "ODD"
    else:
        return "even"
print(is_even(14))  
print(is_even(17)) 