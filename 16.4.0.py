n=int(input())
lista=list((input().upper()).split())
lista2=lista[:]
#print(lista)
for i in range(5):
    toy,dire,casa=(input().upper()).split()
    casa=int(casa)
    x=lista2.index(toy)
    
    if casa==0:
        continue
    if dire=='D':
        if x==len(lista2)-1:
            old=lista2[0]
            lista2[0]=toy
            for i in range(1,len(lista2)):
                lista2[i]=old
                old=lista2[i]
            #print(lista2)
        else:
            lista2.insert(x+casa+1,toy)
            lista2.remove(toy)
            #print(lista2)
    elif dire=='E':
        lista2.remove(toy)
        lista2.insert(x-casa,toy)
        #print(lista2)
dif=0
for i in range(n):
    if lista2[i]!=lista[i]:
        dif+=1
print(dif)
