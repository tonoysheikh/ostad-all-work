def add(num):
    if num:
        return num + add(num-1)
    else:
        return 0

n = int(input("Enter the value of n : "))     
res = add(n)
print("Your result is" , res)