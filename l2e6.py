ha, ma, hb, mb = input().split()
ha, ma, hb, mb = [int(ha), int(ma), int(hb), int(mb)]
inicio =float( ha+ (ma/60))
final = float(hb + (mb/60))
total = float(24 -( inicio-final ))
horas = int(total%24)
minutos = (int(total*60)%60)
if ha == ma == hb == mb:
    print('O jogo durou', 24,'hora(s) e' ,00,'minuto(s).')
else:
    print('O jogo durou', horas,'hora(s) e' ,minutos,'minuto(s).')
