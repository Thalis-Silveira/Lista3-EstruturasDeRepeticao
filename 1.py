numeros = []
num = int(input("Digite um numero:"))

ateVinteECinco = []
ateCinquenta = []
ateSetentaECinco = []
ateCem = []

while(num >= 0):
    numeros.append(num)
    num = int(input("Digite um numero:"))


for i in range(len(numeros)):
    if(75 < numeros[i] <= 100):
        ateCem.append(numeros[i])
    elif(50 < numeros[i] <= 75):
        ateSetentaECinco.append(numeros[i])
    elif(25 < numeros[i] <= 50):
        ateCinquenta.append(numeros[i])
    elif(0 <= numeros[i] <= 25):
        ateVinteECinco.append(numeros[i])

print(f"numeros entre[0-25]: {ateVinteECinco}\nnumeros entre[26-50]:{ateCinquenta}\nnumeros entre[51-75]:{ateSetentaECinco}\nnumeros entre[76-100]:{ateCem}")