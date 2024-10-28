n1 = float(input("Nota1 :"))
n2 = float(input("Nota2 :"))
n3 = float(input("Nota3 :"))
n4 = float(input("Nota4 :"))
media = (n1 + n2 + n3 + n4) / 4

print (f"Media: {media}")

print ("-----------------------")

if media >= 7:
    print ("Aluno aprovado!")

if media < 5:
    print ("Aluno reprovado!")

if media > 5 and media < 6.9:
    print ("Aluno em exame!")

    print ("-----------------------")

    exame = float(input("Nota do exame:"))

    exame = (media + exame) / 2

    print ("-----------------------")

    if exame >= 5:
        print ("Aluno aprovado!")

    if exame < 5:
        print ("Aluno reprovado!")

    print ("-----------------------")

    print (f"Media final: {exame}")