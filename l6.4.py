n = int(input())
lista = input()
lista = lista.split(' ')
nova = lista
lista = tuple(lista)
print(lista)
for i in range(5):
    toy, way, casas = input().split()
    casas = int(casas)
    x = nova.index(toy)
    if casas != 0:
        nova.remove(toy)
        if way == 'D':
            nova.insert(x+casas, toy)
        elif way == 'E':
            nova.insert(x-casas, toy)
nova = tuple(nova)
dif = 0
for i in range(n):
    if lista[i] != nova[i]:
        dif = dif + 1
print(dif)
