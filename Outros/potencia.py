def potencia(num,cont):
    if cont == 2:
        return num
    else:
        return num*potencia(num,cont+1)
cont = 1
print(potencia(5,cont))
