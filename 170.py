
#Variables
Cantidad_Cartas=1
Ultima_Carta="Null"
Termino = True
unos=[]
dos=[]
tres=[]
cuatros=[]
cincos=[]
seis=[]
sietes=[]
ochos=[]
nueves=[]
diez=[]
jotas=[]
qus=[]
rey=[]
contador = 1
lectura=input()
#Ciclo de rellenado
"""
if " " in lectura:
    cartas=lectura.split()
    unos.insert(3,cartas[0])
    unos.insert(2,cartas[13])
    unos.insert(1,cartas[26])
    unos.insert(0,cartas[39])
    dos.insert(3,cartas[1])
    dos.insert(2,cartas[14])
    dos.insert(1,cartas[27])
    dos.insert(0,cartas[40])
    tres.insert(3,cartas[2])
    tres.insert(3,cartas[15])
    tres.insert(3,cartas[28])
    tres.insert(3,cartas[41])
    cuatros.insert(3,cartas[2])
"""
if True:
    while(lectura != "#"):
        print("ENTRO")
        if contador == 1 and lectura != " ":
            unos.insert(0,lectura)
        elif contador == 2 and lectura != " ":
            dos.insert(0,lectura)
        elif contador == 3 and lectura != " ":
            tres.insert(0,lectura)
        elif contador == 4 and lectura != " ":
            cuatros.insert(0,lectura)
        elif contador == 5 and lectura != " ":
            cincos.insert(0,lectura)
        elif contador == 6 and lectura != " ":
            seis.insert(0,lectura)
        elif contador == 7 and lectura != " ":
            sietes.insert(0,lectura)
        elif contador == 8 and lectura != " ":
            ochos.insert(0,lectura)
        elif contador == 9 and lectura != " ":
            nueves.insert(0,lectura)
        elif contador == 10 and lectura != " ":
            diez.insert(0,lectura)
        elif contador == 11 and lectura != " ":
            jotas.insert(0,lectura)
        elif contador== 12 and lectura != " ":
            qus.insert(0,lectura)
        elif contador == 13 and lectura != " ":
            rey.insert(0,lectura)
        contador+=1
        lectura=input()
        if contador == 14:
            contador = 1
    
Ultima_Carta = rey[0]
rey.pop(0)
print("SALIO")
while(Termino):
    if (Ultima_Carta[0] == 'A'):
        if(len(unos)== 0):
            Termino = False
            Cantidad_Cartas+=1
        else:
            Ultima_Carta = unos[0]
            unos.pop(0)
            Cantidad_Cartas+=1
    if (Ultima_Carta[0] == '2'):
        if(len(dos)== 0):
            Termino = False
            Cantidad_Cartas+=1
        else:
            Ultima_Carta = dos[0]
            dos.pop(0)
            Cantidad_Cartas+=1
    if (Ultima_Carta[0] == '3'):
        if(len(tres)== 0):
            Termino = False
            Cantidad_Cartas+=1
        else:
            Ultima_Carta = tres[0]
            tres.pop(0)
            Cantidad_Cartas+=1
    if (Ultima_Carta[0] == '4'):
        if(len(cuatros)== 0):
            Termino = False
            Cantidad_Cartas+=1
        else:
            Ultima_Carta = cuatros[0]
            cuatros.pop(0)
            Cantidad_Cartas+=1
    if (Ultima_Carta[0] == '5'):
        if(len(cincos)== 0):
            Termino = False
            Cantidad_Cartas+=1
        else:
            Ultima_Carta = cincos[0]
            cincos.pop(0)
            Cantidad_Cartas+=1
    if (Ultima_Carta[0] == '6'):
        if(len(seis)== 0):
            Termino = False
            Cantidad_Cartas+=1
        else:
            Ultima_Carta = seis[0]
            seis.pop(0)
            Cantidad_Cartas+=1
    if (Ultima_Carta[0] == '7'):
        if(len(sietes)== 0):
            Termino = False
            Cantidad_Cartas+=1
        else:
            Ultima_Carta = sietes[0]
            sietes.pop(0)
            Cantidad_Cartas+=1
    if (Ultima_Carta[0] == '8'):
        if(len(ochos)== 0):
            Termino = False
            Cantidad_Cartas+=1
        else:
            Ultima_Carta = ochos[0]
            ochos.pop(0)
            Cantidad_Cartas+=1
    if (Ultima_Carta[0] == '9'):
        if(len(nueves)== 0):
            Termino = False
            Cantidad_Cartas+=1
        else:
            Ultima_Carta = nueves[0]
            nueves.pop(0)
            Cantidad_Cartas+=1
    if (Ultima_Carta[0] == 'T'):
        if(len(diez)== 0):
            Termino = False
            Cantidad_Cartas+=1
        else:
            Ultima_Carta = diez[0]
            diez.pop(0)
            Cantidad_Cartas+=1
    if (Ultima_Carta[0] == 'J'):
        if(len(jotas)== 0):
            Termino = False
            Cantidad_Cartas+=1
        else:
            Ultima_Carta = jotas[0]
            jotas.pop(0)
            Cantidad_Cartas+=1
    if (Ultima_Carta[0] == 'Q'):
        if(len(qus)== 0):
            Termino = False
            Cantidad_Cartas+=1
        else:
            Ultima_Carta = qus[0]
            qus.pop(0)
            Cantidad_Cartas+=1
    if (Ultima_Carta[0] == 'K'):
        if(len(rey)== 0):
            Termino = False
            Cantidad_Cartas+=1
        else:
            Ultima_Carta = rey[0]
            rey.pop(0)
            Cantidad_Cartas+=1
print(str(Cantidad_Cartas)+","+Ultima_Carta)
#
"""
TS QC 8S 8D QH 2D 3H KH 9H 2H TH KS KC
9D JH 7H JD 2S QS TD 2C 4H 5H AD 4D 5D
6D 4S 9S 5S 7S JS 8H 3D 8C 3S 4C 6S 9C 
AS 7C AH 6H KD JC 7D AC 5C TC QD 6C 3C
# 
"""