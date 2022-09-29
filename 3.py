from itertools import count


print("###################################################\n1-Maria\n2-Joao\n3-Claudia\n4-Apolosclay\n5-Voto nulo\n6-voto em branco\n###################################################")


Maria = []
Joao = []
Claudia = []
Apolosclay = []
VotosNulos = []
VotosEmBranco = []

numero = [1,2,3,4,5,6]

votos = [4,2,6,5,1,4,4,4,5,1,2,3,1,4,5,4,6]
for i in  range(len(votos)):
    if(votos[i] == 1):
        Maria.append(votos[i])
    elif(votos[i] == 2):
        Joao.append(votos[i])
    elif(votos[i] == 3):
        Claudia.append(votos[i])
    elif(votos[i] == 4):
        Apolosclay.append(votos[i])
    elif(votos[i] == 5):
        VotosNulos.append(votos[i])
    else:
        VotosEmBranco.append(votos[i])

percentagemNulos = (len(VotosNulos)/len(votos)) * 100
percentagemBranco =(len(VotosEmBranco)/len(votos)) * 100
print(f"###################################################\nContagem de votos\n1-Maria: {len(Maria)}\n2-Joao: {len(Joao)}\n3-Claudia: {len(Claudia)}\n4-Apolosclay: {len(Apolosclay)}\n5-Voto nulo: {len(VotosNulos)}\n6-voto em branco: {len(VotosEmBranco)}\nPercentual de votos nulos: {(percentagemNulos):.2f} %\nPercentual de votos em branco: {(percentagemBranco):.2f} %\n###################################################")
print(len(votos))