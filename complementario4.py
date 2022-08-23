from ctypes.wintypes import PLARGE_INTEGER
from string import octdigits


dia=int(input("ingrese el dia"))
mes=int(input("ingrese el mes"))
ano=int(input("ingrese el año"))

if dia>0 and dia<30:
    print("mañana es ",dia+1)
    print("/",mes,"/",ano)
else:
    if mes<12 and mes>0:
        print("mañana es 1/",mes+1,"/",ano)
    else:
        print("mañana es 1/1/",ano+1)