
x1,y1 = (input().split())

x2 , y2 = (input().split())
x1,y1,x2,y2 = [float(x1),float(y1),float(x2),float(y2)]
dist = (((x1-x2)**2) + ((y1-y2)**2))**(1/2)

cplx = complex(input())
mod =  ((cplx.real)**2 + (cplx.imag)**2)**(1/2)
print("%.4f"%dist)
print("%.4f"%mod)
