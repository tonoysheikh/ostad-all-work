def fect(num):
    if num == 0:
        return 1
    else:
        return num * fect(num-1)

n = int(input("Enter your number :"))
res = fect(n)

print("Factorial of",n,"is",res)