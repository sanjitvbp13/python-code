#program to chrck whether a number is even or odd without modilas(%) operator.
#method_1
def is_even(n):
    if n == 0:
        return True
    elif n == 1:
        return False
    else:
        return is_even(n - 2)

print(is_even(14))  
print(is_even(17))  