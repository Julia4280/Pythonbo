def crear_repetits(a,b):
    c = b*int(a)
    return c
x= input("Introdueix un número: ")
y= input("Introdueix un caàcter: ")
print("El caràcter" ,y, "repetit" ,x, "-cegades és: " , crear_repetits(x,y))