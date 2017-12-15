def somatorio(num,cont):
    if cont == num:
        return cont
    else:
        return cont + somatorio(num,cont+1)
    """ou
     if num == 0:
       return num
     else:
       return num+somatorio(num-1)"""
cont = 0
print(somatorio(10,cont))
