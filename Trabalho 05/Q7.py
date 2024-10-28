produtos = {
    1: "Milkshake",
    2: "Hamburguer",
    3: "Sorvete",
    4: "Refrigerante"
}

codigo = int(input("Digite o código do produto: "))

if codigo in produtos:
    print("Produto: ", produtos[codigo])
else:
    print("Código inválido")