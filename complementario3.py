


P=float(input("ingrese el precio "))
M=input("ingrese la marca ")
Pt=float
Pa=float
if P>2000.0 and M=="NOSY":
    Pt=P*0.8

    Pa=Pt*1.20
    print ("el precio es: ",Pa," pesos")

elif P>2000.0 and M!="NOSY":
    Pt=P*0.90
    Pa=Pt*1.20
    print ("el precio es: ",Pa," pesos")

elif P<2000.0 and M=="NOSY":
    Pt=P*0.95
    Pa=Pt*1.20
    print ("el precio es: ",Pa," pesos")

elif P<2000.0 and M!="NOSY":
    Pa=P*1.20
    print ("el precio es: ",Pa," pesos")

