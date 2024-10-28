def notas (n1, n2, n3):
    media = (n1 + n2 + n3) / 3
    if media >= 7:
        print ("Aprovado")
    else:
        print ("Prova final")
        pf = float(input("Digite a nota da prova final:"))
        if pf >= 7:
            print ("Aprovado")
        else:
            print ("Muito Burro kkkkkkkk")
        

n1 = float(input("Digite sua primeira nota:"))
n2 = float(input("Digite sua segunado nota:"))
n3 = float(input("Digite sua terceira nota:"))

notas (n1, n2, n3)