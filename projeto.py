y = 1          #declaraçao da variavel que controla o fim do programa
teste = 0      #declaraçao da variavel auxiliar que recebe a media do competidor anterior
campeao = "nao definido"   #tira a mensagem de erro do pycharm (no fim nao serve pra nada)
r = input("Deseja iniciar o programa? Digite 's' ou 'n':")  #input para iniciar o programa
while r != "s" and r != "n":            #enquanto a resposta for diferente de "s" ou "n" o laço continua
    r = input("Digite uma resposta valida!:")

while r == "s":            #se a resposta for "s" o programa inicia
    media = 0              #declaraçao da var media
    na = input("Digite o nome do atleta:")  #input do nome do atleta
    x = 1               #declarçao da variavel que controla o laço dos saltos
    maior = -99999      #valores extremos nas variaveis para garantir que o primeiro numero vai ser atribuido-
    menor = 99999       #-em maior ou menor

    while x <= 5:       #5 saltos - 5 voltas no loop
        s = float(input(f"Insira o {x}° salto em m:"))  #input dos saltos
        while s < 0:           #caso o numero inserido seja negativo
            s = float(input("Digite um numero valido:"))
        if s > maior:       #se o numero atual for maior que a var "maior" o posto é tomado
            maior = s
        if s < menor:       #se o numero atual for menor que a var "menor" o posto é tomado
            menor = s
        media = media + s   #soma da media
        x = x + 1

    media = media - (maior + menor)         #é retirado os valores maior e menor da media
    media = media / 3                       #media final

    print(f"\nMelhor salto: {maior}m")
    print(f"Pior salto: {menor}m")
    print(f"Media dos saltos: {media:.1f}m\n")
    print(f"Resultado final:\n{na}: {media:.1f}m\n")

    r = input("Deseja continuar o programa? Digite 's' ou 'n':")    #input para continuar o programa

    while r != "s" and r != "n":           #enquanto a resposta for diferente de "s" ou "n" o laço continua
        r = input("Digite uma resposta valida!:")

    if media >= teste:      #testa se o valor da media atual é maior que a anterior/caso haja um empate o operador ">="
        teste = media
        campeao = na        #faz com que o valor atual igual ao anterior receba o posto de campeao
    y = 2           #variavel de controle caso o usuario decida nao iniciar o programa (linha 4)

if y == 2:          #apenas acontece caso o usuario decida iniciar o programa
    print(f"ATLETA CAMPEÃO: {campeao.upper()}\n")   #declara o campeao em letra maiuscula pela funçao .upper()
