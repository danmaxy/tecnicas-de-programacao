dia = int(input("Digite o dia:"))
mes = int(input("Digite o mes:"))
ano = int(input("Digite o ano:"))
print ("---------------------")

if dia <= 31 and dia >= 1 and mes >= 1 and mes <= 12 and ano >= 1:
    print ("Data Valida")
else:
    print ("Data Invalida")