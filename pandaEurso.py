n = int(input())
u = 0
p = 0
for i in range(0,n):
    x = input()
    u = u + x.count('u')+x.count('U')
    p = p + x.count('p')+x.count('P')
print(p,u)
