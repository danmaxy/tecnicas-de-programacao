salario = float(input("Digite seu salario:"))
aumento = 0

if salario > 1250:
    aumento = (salario) * 0.10
else:
    aumento = (salario) * 0.15

salario = salario + aumento
print (f"Aumento: R${aumento} \nNovo salario: R${salario}")