from xml.etree.ElementTree import PI


print("1 area de triangulo, 2 area de circulo")
r=int(input())
if r==1:
    print ("ingrese el lado de triangulo")
    l=float(input())
    re=float
    re=(((l**2)+((l/2)**2)**0.5)*l)/2
    print ("el area es ",re)
else:
    print("ingrese el radio del circulo")
    ra=float(input())
    re=3.14159268*ra**2
    print ("el area es ",re)
