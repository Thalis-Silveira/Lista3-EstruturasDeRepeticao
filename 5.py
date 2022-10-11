nomes = []
saltos = []
salto = []
melhor = []
pior = []
nome = input("nome:")
while (nome != ""):
    nomes.append(nome)
    for i in range(0,5):
        jump = float(input(f"Digite o {i + 1}º salto: "))
        salto.append(jump)
    saltos.append(list(salto))
    salto.clear()
    nome = input("nome:")

for i in range(len(saltos)):      
    print(f"Atleta: \t{nomes[i]}")
    for h in range(len(saltos[i])):
        print(f"{h + 1}º Salto:\t{saltos[i][h]}")
    
    saltos[i].sort()
    melhor.append(saltos[i][-1])
    pior.append(saltos[i][0])
    saltos[i].pop(0)
    saltos[i].pop(-1) 
    print(f"Melhor salto:\t{melhor[i]}")
    print(f"Pior salto:\t{pior[i]}")

    print("Média dos demais saltos: \t{:.2f}".format(sum(saltos[i])/len(saltos[i])))
