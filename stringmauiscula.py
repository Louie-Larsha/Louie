x = input()
y = x.split('.')
c = ''
p = '.'
for i in y:
    if i[0] != ' ':
        c = c + i[0].upper + i[1::]
    else:
        c = c + i[0] + i[1].upper()+ i[2::]
    c = c+i+p
print(c)
