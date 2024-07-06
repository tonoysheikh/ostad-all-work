def fun(ls1):
    reverse_ls = [s[::-1] for s in ls1]
    return reverse_ls

ls = ["Hello" , "Python" , "coding"]
print(fun(ls))

