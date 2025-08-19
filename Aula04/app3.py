#Importando bibliotecas (lib)
import random
lista = []
sair = False

while sair == False:
    nome_candidato = input('Digite os nomes para o sorteio ou enter para sair: ')
    if nome_candidato != "":
        #append - adiciona o valor da variavel na lista
        lista.append(nome_candidato)
    else:
        sair = True
escolhido = random.choice(lista)
print('O Candidato escolhido foi', escolhido)
