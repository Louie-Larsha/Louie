x = input()
minuscula = 'abcdefghijklmnopqrstuvwxyz'
maiuscula = minuscula.upper()
num = '1234567890'
c = ''
for i in range(0,len(x)):
    if x[i] in maiuscula:
        c = c+'U'
    elif x[i] in minuscula:
        c = c + 'L'
    elif x[i] in ' ':
        c = c+'W'
    elif x[i] in num:
        c = c+'D'
print(c)
