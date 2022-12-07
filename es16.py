def invertir(a):
    b = list(a)
    c = b[::-1]
    r = " ". join(c)
    return r

#pp
b = input("Introdueix una paraula")
c = invertir(b)
print("La paraula" ,b, "Si la giram és", c)