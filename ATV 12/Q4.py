idades = [18, 19, 15, 14, 16, 20, 21, 13, 15, 18]
x = 0
for i in idades:
    if i >= 18:
        x = x + 1
print (f"{x} -- sao maiores de idade")

x = 0
for i in idades:
    if i < 18:
        x = x + 1
print (f"{x} -- sao menores de idade")

x = 0
for i in idades:
    if i == 15:
        x = x + 1
print (f"{x} -- tem 15 anos")