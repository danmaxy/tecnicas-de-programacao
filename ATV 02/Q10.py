bruto = float(input("Digite o salario bruto: "))
inss = 15
ir = 10
calculo1 = (bruto * inss) / 100
calculo2 = (bruto * ir) / 100
print (f"Valor descontado pelo INSS: -{calculo1}")..
print (f"Valor descontado pelo IR: -{calculo2}")
resultado = bruto - calculo1 - calculo2
print()
print (f"Salario liquido: {resultado}")

