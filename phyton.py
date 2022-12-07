a=(1, 2, 4, 8, 16, 32, 64)
i=0
for c in a:
    a[1]=c+1
    print(a[i])
    i+=1

b = ['h', 'o', 'l', 'a']
for c in b:
    print(c)


a.append(128)
print(a)

b.extend(['P', 'e', 'r', 'e'])
print(b)


c = a + b
print(a)

c.intert(9,256)
print(c)