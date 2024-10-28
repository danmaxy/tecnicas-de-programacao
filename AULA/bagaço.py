rendimento = float(input("Digite o rendimento:"))

if rendimento <= 7112:
    imposto = (rendimento * 14.5) / 100
    print (imposto)

if rendimento > 7112 and rendimento < 10732 :
    imposto = (rendimento * 23) / 100
    print (imposto)

else:
    imposto = (rendimento * 48) / 100
    print (imposto)