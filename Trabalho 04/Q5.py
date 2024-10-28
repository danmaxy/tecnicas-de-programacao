salario = float(input("Digite seu salrio:"))
imposto = 0
inss = 0

if salario > 2000:
    imposto = salario * 0.15
    inss = salario * 0.10
else:
    imposto = 0
    inss = 0

liquido = salario - imposto - inss

print (f"Salario: R${salario} \nImposto de renda: R${imposto} \nINSS: R${inss}")
print (f"Salario liquido: R${liquido}")