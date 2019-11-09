m , d = input().split()
m , d = [int(m), int(d)]
c = int()
import math

if m == 2:
    c = math.ceil((28 + (d-1))/7)
    print(c)

elif m == 1 or m ==3 or m== 5 or m== 7 or m ==8 or m ==10 or m ==12 :
    c = math.ceil((31 + (d-1))/7)
    print(c)

elif m == 4 or m== 6 or m== 9 or  m==11:
    c = math.ceil((30 + d - 1)/7)
    print(c)

