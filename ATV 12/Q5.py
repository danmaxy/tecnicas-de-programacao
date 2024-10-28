salarios = [2000, 1700, 1500, 1300, 2500, 3000, 2600, 4000, 1000, 700, 900, 6000, 10000]
x = 0
for i in salarios:
    x = x + i
print (x)

x = 0
for i in salarios:
    if i > 1000.50:
        x = x + i
print (x)