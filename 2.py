pedidoTotal = []
codigo = [100,101,102,103,104,105]
valores =  [1.20,1.30,1.50,1.20,1.30,1.00]

cont = "S"
while(cont != "N"):
    pedido = int(input("Digite o codigo do pedido: "))
    quant = int(input("Quantidade: "))
    for i in range(len(codigo)):
            if(pedido == codigo[i]):
                pedidoTotal.append(valores[i] * quant)
    if(pedido not in codigo):
        print("Codigo do pedido não existe!")
    if(quant <= 0):
        print("Quantidade inválida, digite novamente abaixo")
        while(quant<=0):   
            quant = int(input("Quantidade: "))

    cont = input("Deseja continuar[S/N]: ").upper()
    
print("Valor a ser pago R$ {:.2f}".format(sum(pedidoTotal)))
