gabarito = ["A","B","C","D","E","E","D","C","B","A"]
acertos = []
continuar = "S"
resposta = []
total = 0

while(continuar != "N"):
    for i in range(len(gabarito)):
        resp = input("Digite a resposta: ").upper()
        if(gabarito[i] == resp):
            resposta.append(resp)
    acertos.append(list(resposta))
    total += len(resposta)
    resposta.clear()
                        

    continuar = input("Algum aluno ainda usará o sistema[S/N]: ").upper()
maiorAcerto = 0
menorAcerto = 10
for i in range(len(acertos)):
    for j in range(len(acertos[i])):
        if(len(acertos[i]) > maiorAcerto):
            maiorAcerto = len(acertos[i])
        elif(len(acertos[i]) < menorAcerto):
            menorAcerto = len(acertos[i])
    print("O aluno {}, acertou {} questões.".format(i + 1, len(acertos[i])))

print(f"Sendo o maior numero de acertos = {maiorAcerto} e o menor = {menorAcerto}\tO total de alunos foi de {len(acertos)}\tE com média da turma = {total/(len(acertos))}")


