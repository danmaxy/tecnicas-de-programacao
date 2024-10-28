a = float(input("Valor:"))
b = float(input("Valor:"))
c = float(input("Valor:"))
import math
print("-------------")
delta = b**2 - 4*a*c

if a == 0:
    print ("Impossivel calcular")
else:
    x1 = (-b + math.sqrt(delta)) / (2*a)
    x2 = (-b - math.sqrt(delta)) / (2*a)
    print (f"R1: {x1} \nR2: {x2}")