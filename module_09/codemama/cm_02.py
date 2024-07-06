
x,y = map(float, input().split())

res = y/x**2
res = format(res ,".2f")
res = float(res)
print("BMI:",res)

if(res < 18.5):
    print("Underweight")
elif(res >= 18.5 and res < 25.0):
    print("Normal weight")
elif(res >= 25.0 and res < 30.0):
    print("Overweight")
else:
    print("Obese")