p = float(input())
h = float(input())
imc = p/(h**2)
perder = p - 24.9 * h**2

print ("%.2f"%imc)

if imc < 18.5:
    print('Baixo peso')
elif imc >= 18.5 and imc <24.9:
    print('Peso normal')
elif imc >= 24.9 and imc<29.9:
    print('Sobrepeso')
    print("%.2f"%perder)
elif imc >= 29.9 and imc < 34.9:
    
    print('Obesidade Grau I')
    print("%.2f"%perder)
elif imc >= 34.9 and imc< 39.9:
    print('Obesidade Grau II')
    print("%.2f"%perder)
elif imc >= 39:
    print('Obesidade Grau III')
    print("%.2f"%perder)
