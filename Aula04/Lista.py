'''= lista 
nomes_lista = ('fulano','citrano', 'beltrano', 'joana','maria', 'mariano')
print(nome_lista[0]) #exibindo o primeiro nome da lista 
print(nome_lista[2]) #exibindo o segundo nome da lista 
print(nome_lista[5]) #exibindo o quinto nome da lista 

for nome in nomes_lista:
    print(nome)


nomes_lista = ('fulano','citrano', 'beltrano', 'joana','maria', 'mariano')
#percorrendo a lista com um contador 
for i in range (len(nomes_lista)):
    print(f'{i + 1}º nome da lista: {nomes_lista[i]}')
    
nomes_lista = ['Fulano', 'Cicrano', 'Beltrano', 'Joano', 'Mario', 'Mariano']
nome = input('Informe o nome que deseja encontrar: ')
#Busca o nome desejado na lista
if nome in nomes_lista:
    print(nome,", Encontrado na lista!")
else:
    print(f'{nome} não encontrado')
#Busca o nome desejado na lista
for i in range (5):
    

nomes_lista = ['Fulano', 'Cicrano', 'Beltrano', 'Joano', 'Mario', 'Mariano']
nome = input('Informe o nome que deseja encontrar: ')  
indice = nomes_lista.index(nome)

try: 
    print(f'{nome}encontrado no indice {indice}')
except:
    print(f'{nome} nao encontrado.')

    
nomes_lista = ['Fulano', 'Cicrano', 'Beltrano', 'Joano', 'Mario', 'Mariano']
nome = input('Informe o nome que deseja encontrar: ') 
quantidade = nomes_lista.count(nome)

try: 
    print(f'{nome}foi encontrado na lista{quantidade}vezes.')
except:
    print(f'{nome}nao encontrado na lista. ')
 

nomes_lista = ['Fulano', 'Cicrano', 'Beltrano', 'Joano', 'Mario', 'Mariano']
nomes_lista[0] = 'Andre'

for nome in nomes_lista:
    print(nome)

#Tabuada
numero = int(input('Digite o número: '))

for i in range(1, 11):
    resultado = numero * i
    print(f'{i} X {numero} = {resultado}')
'''