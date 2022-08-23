print("ingrese las velocidades de los veiculos")
V1=float(input())
V2=float(input())
print("ingrese la distancia que los separa")
d=float(input())
t=float
if V1>0 and V2>0:
    t=d/(V1+V2)
    print(t," segundos")
else:
    print("ERROR")