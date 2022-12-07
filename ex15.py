def sumarllista (a):
    sumatori = 0
    for i in a:
        sumatori += i
    return sumatori

def multiplicarllista (b):
    multiplicatori = 1
    for i in b:
        multiplicatori *= i
    return multiplicatori

x = [1,3,4,5,7]
print("La suma dels elements de la llista és: ",sumarllista(x))
print("La multiplicació dels elements de la llista és: ",multiplicarllista(x))
