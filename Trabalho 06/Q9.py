print ("1 - Adicionar")
print ("2 - Editar")
print ("3 - Pesquisar")
print ("4 - Remover")
print ("0 - Sair")

num = int(input("Escolha uma opcao:"))

print ("---------------------")

if num == 1:
    print ("Vc escolheu Adicionar")
elif num == 2:
    print ("Vc escolheu Editar")
elif num == 3:
    print ("Vc escolheu Pesquisar")
elif num == 4:
    print ("Vc escolheu Remover")
elif num == 0:
    print ("Vc escolheu Sair")
else:
    print ("Opcao invalida")

