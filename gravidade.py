n =  int(input())
lista=[]
for i in range(n):
    x = input()
    x= x.split(' ')
    lista = lista + [x]

#print(lista)
for i in range(n-1):
    for p in range(n):
        if 'o' == lista[i][p] and n!= 1:
            if lista[i+1][p] == '.':
                lista[i][p]= '.'
                lista[i+1][p] = 'o'
#print(lista)
for i in range(1):
    for p in range(n):
        if 'o' == lista[i][p]and n!=1:
            if lista[i+1][p] == '.':
                lista[i][p]= '.'
                lista[i+1][p] = 'o'
p = 0
for i in x:
    print(' '.join(lista[p]))
    p = p+1
