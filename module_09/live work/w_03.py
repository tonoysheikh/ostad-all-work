def fun(ls):
    swap_ls = [(b,a) for a,b in ls]
    return swap_ls   
    
ls = [(1,2) , (3,4)]
print(fun(ls))