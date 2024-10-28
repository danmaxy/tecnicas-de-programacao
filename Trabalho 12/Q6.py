nomes = ["Alice", "Bob Charlton", "Carlos", "Diana", "Eva"]
notas = [8.5, 9.0, 7.5, 6.0, 9.3]

resultado = zip (nomes, notas)
for nomes, notas in resultado:
    print (f"{nomes}: {notas}")