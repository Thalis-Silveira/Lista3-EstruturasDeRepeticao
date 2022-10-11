candidato = []
notas = []
nomes = []
melhor = []
pior = []

cont = "S"
while(cont != "N"):
    nome = input("Nome: ")
    nomes.append(nome)
    for i in range(1,8):
        nota = float(input("Nota: "))
        notas.append(nota)
    candidato.append(list(notas))
    notas.clear()
    
    cont = input("continuar[s/n]:").upper()

print("Resultado")
for i in range(len(candidato)):      
    print(f"Atleta: \t{nomes[i]}")
    
    candidato[i].sort()
    melhor.append(candidato[i][-1])
    pior.append(candidato[i][0])
    candidato[i].pop(0)
    candidato[i].pop(-1) 
    print(f"Melhor salto:\t{melhor[i]}")
    print(f"Pior salto:\t{pior[i]}")

    print("Média dos demais saltos: \t{:.2f}".format(sum(candidato[i])/len(candidato[i])))
