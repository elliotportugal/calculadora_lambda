calculadora = {
    "soma": lambda a, b: int(a + b),
    "subtracao": lambda a, b: a - b,
    "multiplicacao": lambda a, b: a * b,
    "divisao": lambda a, b: a / b, 
}

soma = calculadora["soma"]
subtracao = calculadora["subtracao"]
multiplicacao = calculadora["multiplicacao"]
divisao = calculadora["divisao"]

rep = "s"

while rep == "s":
    print("=====Bem-vindo à calculadora Python!=====")
    
    opcao = int(input("Selecione a operação desejada: \n1- Soma \n 2- Subtração \n 3- Multiplicação \n 4- Divisão \n 5- Sair\n"))
    if opcao == 1:
        a = int(input("Selecione o primeiro número: "))
        b = int(input("Selecione o segundo número: "))
        resultado = soma(a,b)
        print("O resultado da soma entre {} e {} é: {}".format(a,b, resultado))
    
    elif opcao == 2:
        a = int(input("Selecione o primeiro número: "))
        b = int(input("Selecione o segundo número: "))
        resultado = subtracao(a,b)
        print("O resultado da subtração entre {} e {} é: {}".format(a,b, resultado))

    elif opcao == 3:
        a = int(input("Selecione o primeiro número: "))
        b = int(input("Selecione o segundo número: "))
        resultado = multiplicacao(a,b)
        print("O resultado da multiplicação entre {} e {} é: {}".format(a,b, resultado))

    elif opcao == 4:
        a = int(input("Selecione o primeiro número: "))
        b = int(input("Selecione o segundo número: "))
        resultado = divisao(a,b)
        print("O resultado da divisão entre {} e {} é: {}".format(a,b, resultado))

    elif opcao == 5:
        print("Você está saindo")

    elif opcao > 5:
        print("A opção invalida")
        
    rep = str(input("Deseja realizar outra operação? [S]im [N]ão: "))
    while rep != 's' and rep != 'n':
        rep = str(input("Entre com um valor valido: "))

print("Obrigado, volte sempre!")