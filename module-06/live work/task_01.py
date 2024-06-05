def fac(num):
    if num:
        return (num * fac(num - 1)) 
    else:
        return 1 
         

n = int(input())
res = fac(n)
print(res)