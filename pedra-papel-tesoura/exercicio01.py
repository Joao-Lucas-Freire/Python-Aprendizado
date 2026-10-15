#Criando um jogo de Pedra Papel e tesoura com Python

#Criando a variaveis para receber o nome dos jogadores
nome01=input("Digite seu nome jogador: ")
nome02=input("Digite seu nome jogador: ")
print("-" * 60) # Criando uma linha para melhor visualização

#Criando uma tupla com as jogadas possiveis
jogadas = ("pedra", "papel", "tesoura")
#printando sejam bem vindos e mostrando as jogadas possiveis aos jogadores
print(f"Sejam bem vindos ao jogo e uma ótima partida \n não esqueçam só podem ultilizar {jogadas}")
print("-" * 60)
#Criando variaveis para receber as jogadas dos usuario
jogada01 = input(f"Faça sua jogada {nome01} ")
jogada02 = input(f"Faça sua jogada {nome02} ")
print("-" * 60)
#Tirando possiveis letras maiusculas e espaços no inicio e/ou no fim da input
escolha01 = jogada01.lower().strip()
escolha02 = jogada02.lower().strip()

#Iniciando o processo de validação dos e de resoltados

if escolha01 not in jogadas or escolha02 not in jogadas:  # Se nenhuma das escolhas estão dentre das jogadas mostre mensagem de erro
    print(f"Como eu disse tem que escolher algum desses {jogadas} ")

elif escolha01 == escolha02:
    print(f"Deu empate ambos escolheram {escolha01}!")      # Se ambos escolheram o mesmo mostre empate

elif (escolha01 == "pedra" and escolha02 == "Tesoura") or \
     (escolha01 == "tesoura" and escolha02 == "papel") or \
     (escolha01 == "papel" and escolha02 == "pedra"):
    print(f"Parabens {nome01} Você venceu!!!")
else: print(f"Parabens {nome02} Você venceu!!!")
print("Fim de jogo")
print("-" * 60)