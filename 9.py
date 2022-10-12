print("1 - necessita da esfera\n2 - necessita de limpeza\n3 - necessita troca do cabo ou conector\n4 - quebrado ou inutilizado")
situacao = int(input("Digite o numero da situacao:"))
ne = 0
nl = 0
ntdcc = 0
qi = 0

while(situacao != 0):
    if (1 < situacao > 4):
        print("Situação não reconhecida")
    elif(situacao == 1):
        ne += 1    
    elif(situacao == 2):
        nl += 1
    elif(situacao == 3):
        ntdcc += 1 
    else:
        qi += 1
    situacao = int(input("Digite o numero da situacao:"))


soma = (ne + nl + ntdcc + qi) /100
percentualne = ne/soma
percentualnl = nl/soma
percentualntdcc  = ntdcc/soma
percentualqi = qi/soma
print("1 - necessita da esfera: {:.2f}%\n2 - necessita de limpeza: {:.2f}%\n3 - necessita troca do cabo ou conector: {:.2f}%\n4 - quebrado ou inutilizado: {:.2f}%".format(percentualne,percentualnl,percentualntdcc,percentualqi))