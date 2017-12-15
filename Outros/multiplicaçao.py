def mult(num,quant,cont):
    if cont > quant:
        return num
    else:
        return mult(num,quant,cont + 1) * cont

cont = 1
print(mult(100,2,cont))
