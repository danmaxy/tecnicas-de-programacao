a = float(input("Valor:"))
b = float(input("Valor:"))
c = float(input("Valor:"))

if a == 0:
    print (f"0 raizes")

else:
    delta = b**2 - 4*a*c
    
    if delta > 0:
        print ("2 raizes")
    if delta < 0:
        print ("0 raizes")
    if delta == 0:
        print ("1 raiz")