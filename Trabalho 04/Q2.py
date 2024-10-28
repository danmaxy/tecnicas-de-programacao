velo = int(input("Digite a velocidade:"))
multa = 0

print ("---------------------------")

if velo > 80:
    multa = (velo - 80) * 10
    print (f"Voce foi multado em: {multa} $")