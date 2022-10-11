cont = "S"
salarios = []
sal = []
abonos = []
maior = 0
menor = 0
salario = float(input("Salário: "))
while(salario != 0):
    if(salario < 1000):
        sal.append(salario)
        abono = 100
        abonos.append(abono)
        salario += abono
        salarios.append(salario)
        menor+=1
    elif(salario >= 1000):
        sal.append(salario)
        abono = (salario * 0.2)
        abonos.append(abono)
        salario += abono
        salarios.append(salario)
    else:
        print("Valor não permitido!!!")

    salario = float(input("Salário: "))
for i in range(len(salarios)):
    if(salarios[i] > maior):
        maior = abonos[i]

print("salarios:")
for i in range(len(sal)):
    print(f"Salarios: \t{sal[i]}\tAbono: \t{abonos[i]}\tSalario + abono R$ {salarios[i]}")

print(f"Foram processados {len(abonos)} abonos\nTotal gasto com abonos:  R$ {sum(abonos)}\nValor minimo pago a {menor}\nMaior valor: {maior}")

 
