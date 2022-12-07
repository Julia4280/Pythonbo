def gran_de_tres(a,b,c):
    a=a
    if (a>b):
        if (a>c): 
            a = a
        elif (c>a): 
            a = c
        else: 
            a = a
    elif (b>a): 
        if (b>c):
            a = b
        elif (c>b):
            a = c
    else:
        if (a>c):
            a = a
        elif (c>a):
            a = c
        else:
            a = a
    return

#Aplicació principal
a = int(input("Escriure el primer valor: "))
b = int(input("Escriure el segon valor: "))
c = int(input("Escriure el tercer valor: "))
d = gran_de_tres(a,b,c)
print("El major de ", a, " , " ,b, " , ",c, " és ", d)
        