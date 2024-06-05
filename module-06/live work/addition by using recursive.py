def add(num):
    if num:
        return num + add(num-1)
    else:
        return 0
        
res = add(100)
print(res)