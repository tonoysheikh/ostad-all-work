def fun(numbers):
    even = [num for num in numbers if num%2 == 0 and num != 0]
    return even

ls = [0,1,2,3,4,5,6,7,8,9,10]
print(fun(ls))