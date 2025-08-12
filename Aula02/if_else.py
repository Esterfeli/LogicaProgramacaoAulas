'''
#firme - contatenação com +

nome = 'felix'
idade = 16
altura = 1.55

# saida de dados 
print("ola, meu nome é," + nome + ', tenho' + str(idade) + ' ano de idade')

#FIXME - concatenação com , 
print("ola,meu nome é,", nome,',tenho',idade,'ano de idade')

#FIXME - concatenação com format 
print("ola,meu nome é, {} , tenho {} anos de idade". format(nome,idade))

#FIXME - concatenação com f-string
print(f"ola,meu nome é {type(nome)} e tenho {idade+1} anos de idade")

# eliminando quebra de linha 
print("o sabio sabia", end ='')
print("que o sabia sabia assobiar.")

valor = 1.23456789
# exibindo o valor com duas casas depois da virgula 
print(f'{valor:,.2f}')

print(30*'=')
peso = input('digite seu peso:').replace(',','.')
peso = float(peso)
print(f'{peso:.2f}')
'''
'''

nome_usuario = input("digite o seu nome: ")
print("Seja bem-vindo as aulas do karython,", nome_usuario),                        

#Estrutura de decisão 
nome = 'ester'
idade = 20 
if idade >= 18:
    print(f'{idade} é maior fe idade')
    print('1voce ester dentro do bloco if')
else:
    print(f'{idade} é menor de idade')
    print('voce este dentro do bloca else')
    print('voce este fora da estrutura condicional if else')

    print('Antes do if')
if idade >= 18:
    print('Número Par')
else:
    print('Número Impar')

    # upper - caixa auta 
    #lower - caixa baixa 

print(40*"-", "BOLETIM ESCOLAR", 40*"-")
nome_aluno = input("Digite o nome do aluno: ")
nota1 = float(input("Digite a sua primeira nota:"))
nota2 = float(input("Digite a sua segunda nota:"))
nota3 = float(input("Digite a sua terceira nota:"))
nota4 = float(input("Digite a sua quarta nota:"))

media = (nota1 + nota2 + nota3 + nota4)/4
# >= 7: aprovado
# >= 5: recuperação
# reprovado

if media >= 7: 
    print(f'{nome_aluno} !!!Aluno Aprovado!')
    print(f'Nota 1: {nota1} | Nota 2: {nota2}')
    print(f'Nota 3: {nota3} | Nota 4: {nota4}')
    print(20*'=')
    print(f'Média: {media}')
elif media >= 5:
    print(f'{nome_aluno} Aluno de Recuperação')
    print(f'Nota 1: {nota1} | Nota 2: {nota2}')
    print(f'Nota 3: {nota3} | Nota 4: {nota4}')
    print(20*'=')
    print(f'Média: {media}')
else:
    print(f'{nome_aluno} Aluno Reprovado')
    print(f'Nota 1: {nota1} | Nota 2: {nota2}')
    print(f'Nota 3: {nota3} | Nota 4: {nota4}')
    print(20*'=')
    print(f'Média: {media}')
    '''
'''
    #variaveis

nome = input('digite seu nome:')
idade = int(input('digite sua idade aqui: '))
altura = float(input('digite sua altura: '))

#verifica se o usuario possui os requisitos minimos 
if idade >= 12 and altura >= 1.2:
     print(f'a entrada de {nome}este autorizada. ')
else:
    print(f'a entrada de {nome} nao esta autorizada.')
'''

#variaveis 
nome = 'ester '
idade = ' 24'

#operador ternario 
print (nome, 'é maoir de idade.' if idade >= 18 else 'é menor de idade')

 #if - verdadeiro else - falso