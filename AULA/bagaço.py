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



    #Em Portugal, o Imposto sobre o Rendimento das Pessoas Singulares (IRS) é calculado com base no rendimento anual. Cria um programa em Portugol que peça ao utilizador o rendimento anual e calcule o valor de imposto a pagar com base nos seguintes escalões simplificados:
    #Até 7.112: 14,5%
    #Entre 7.113 e 10.732: 23%
    #Entre 10.733 e 20.322: 28,5%
    #Entre 20.323 e 25.075: 35%
    #Entre 25.076 e 36.967: 37%
    #Entre 36.968 e 80.882: 45%
    #Acima de 80.883: 48%