n = int(input("How many partten you want : "))
print("Your partten is here : ")
cnt = 1
for i in range(0,n+1):
    for j in range(1,cnt+1):
        print(j , end =' ')
    print("")
    if(cnt == n):
        break
    else:
        cnt += 1