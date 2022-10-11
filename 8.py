carros = ["FUSCA","GOL","UNO","VECTRA","PEUGEOUT"]
consumo = [7.0,10.0,12.5,9,14.5]
gasolina = 2.25
eco = []
valPerMil = gasolina * 1000
litrosGastos = []

eco.append(carros[consumo.index(max(consumo))])
for j in range(len(consumo)):
    print("{} - {} - {:.2f} - {:.2f} litros - R$ {:.2f}".format(j + 1,carros[j],consumo[j],(valPerMil/consumo[j])/gasolina,valPerMil/consumo[j]))

print(f"o menor consumo é do{eco}")
