print ("Digite S ou N =>")

print ("------------------")
p1 = input("Ele e vertebrado:")

if p1 == "S":
    p2 = input("Ele e ave:")
    p3 = input("Ele e onivoro:")
else:
    p5 = input("Ele e inseto:")
    p4 = input("Ele e hematofago:")

    if p4 == "N":
        if p5 == "N":
            print ("Resposta: Minhoca")
    if p4 != "N":
        if p5 == "N":
            print ("Resposta: Sanguessuga")
    if p4 == "N":
        if p5 != "N":
            print ("Resposta: Lagarta")
    if p4 != "N":
        if p5 != "N":
            print ("Resposta: Pulga")
if p1 == "S":
    if p2 == "S":
        if p3 == "S":
            print ("Resposta: Pomba")
if p1 == "S":
    if p2 == "S":
        if p3 != "S":
            print ("Resposta: Aguia")
if p1 == "S":
    if p2 != "S":
        if p3 == "S":
            print ("Resposta: Homem")
if p1 == "S":
    if p2 != "S":
        if p3 != "S":
            print ("Resposta: Vaca")