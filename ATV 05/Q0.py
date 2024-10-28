# Cálculo do IRS

rendimento = float(input("Digite o rendimento anual: "))

if rendimento <= 7112:
    imposto = rendimento * 0.145
elif rendimento <= 10732:
    imposto = rendimento * 0.23
elif rendimento <= 20322:
    imposto = rendimento * 0.285
elif rendimento <= 25075:
    imposto = rendimento * 0.35
elif rendimento <= 36967:
    imposto = rendimento * 0.37
elif rendimento <= 80882:
    imposto = rendimento * 0.45
else:
    imposto = rendimento * 0.48

print(f"O imposto a pagar é: {imposto:.2f}")
