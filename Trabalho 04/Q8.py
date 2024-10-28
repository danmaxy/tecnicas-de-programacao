salario = float(input("Digite seu salario:"))
imposto = 0
inss = 0

print ("----------------------")

if salario < 1000:
    print (f"Imposto: {imposto} \nINSS: {inss}")

if salario >= 1000 and salario < 2000:
    imposto = salario * 0.10
    inss = salario * 0.11
    liquido = salario - imposto - inss
    print (f"Imposto: {imposto} \nINSS: {inss} \nLiquido: {liquido}")

if salario >= 2000 and salario < 3000:
    imposto = salario * 0.20
    inss = salario * 0.15
    liquido = salario - imposto - inss
    print (f"Imposto: {imposto} \nINSS: {inss} \nLiquido: {liquido}")

if salario >= 3000:
    imposto = salario * 0.27
    inss = salario * 0.20
    liquido = salario - imposto - inss
    print (f"Imposto: {imposto} \nINSS: {inss} \nLiquido: {liquido}")