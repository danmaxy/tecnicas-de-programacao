imposto = 10

def contracheque (m, f, s1, imposto):
    print ("----------------------------")
    print ("DIVINOS SOFTWARE CARIDADES")
    print (f"MES DE REFERENCIA: {m}")
    print (f"FUNCIONARIO: {f}")
    print ("")
    print (f"DEMONSTRATIVO \nSalario: R$ {s1}")
    print ("")
    imposto = (s1 * imposto) / 100
    print (f"Imposto: {imposto}")
    s1 = s1 - imposto 
    print (f"Total a receber: R$ {s1}")

m = input("Digite o mes:")
f = input("Digite seu nome:")
s1 = float(input("Digite o salario:"))

contracheque (m , f, s1, imposto)