def gran(e,z):
    a=z
    b=e
    if(z>e):
        print(z, "és major" ,e)
    elif(e>z):
        print(e, "és major" ,z)
    else:
        return(e, "es igual que" ,z)
    return a

#Aplicació principal
a=int(input("Escriure el primer valor: "))
b=int(input("Escriure el segon valor: "))
c=gran(a,b)
print("El major de ", a, " i " ,b, " és ", c)