from tkinter import*

n1 = float(input("Nota 1:"))
n2 = float(input("Nota 2:"))
n3 = float(input("Nota 3:"))
n4 = float(input("Nota 4:"))
media = (n1 + n2 + n3 + n4) / 4

print (f"Media: {media}")

if media >= 7:
    print ("Aluno aprovado!")

if media < 5:
    print ("Aluno reprovado!")

if media > 5 and media < 6.9:
    print ("Aluno em exame")

janela = Tk ()
janela.title ("Boletim")

texto_1 = Label (janela, text = "Resultados")
texto_1.grid (column = 1, row = 1)



janela.mainloop ()