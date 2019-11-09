n1, n2 = input().split()
n1, n2 = [int(n1), int(n2)]
lista = list(range(100))
k = lista[n2]
s = ''
for i in range(0,n1):
    f,e = input().split()
    f,e = [str(f), int(e)]
    x = lista[e]
    lista.pop(e)
    if x == k:
        print(f)
