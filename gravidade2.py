n=int(input())
m=[]

for i in range(n):
    m.append(input().split())

for i in reversed(range(n)):
    for j in range(n):
        if m[i][j]=='.':
            if i-1>=0 and m[i-1][j]=='o':
                m[i][j]='o'
                m[i-1][j]='.'
for i in range(n):
    print(' '.join(m[i]),end='')
    print()
