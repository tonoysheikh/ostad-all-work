def fun(ls):
    for i in ls:
        if i % 2 != 0:
            print(i)    

num = input()

n = list(map(int, num.split(',')))

fun(n)
