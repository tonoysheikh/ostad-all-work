x1 , y1 = map(int , input().split())
x2 , y2 = map(int , input().split())

distance = (x2 - x1)**2 + (y2 - y1)**2
distance = distance**0.5

distance = format(distance , ".2f")

print("Distance:",distance)