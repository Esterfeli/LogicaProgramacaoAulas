'''
nome = "Ester"
idade = "16 anos"
numero = "11/01/2009"

print("olá, me chamo", nome, "tenho", idade, "e nasci em", numero)


# Tipos de variaveis 

nome = "Ester"
idade = 16
altura = 1.55
ativo = True 

print("o tipo da variavel nome é:", type(nome))
print("o tipo da variavel idade é:", type(idade))
print("o tipo da variavel altura é:", type(altura))
print("o tipo da variavel ativo é:", type(ativo))

# operadores
print(30*"-","operadores",30*"-")

num1 = 550
num2 = 380

soma = num1 + num2
divi =  num1 / num2
divisao_inteira = num1 // num2
mult =  num1 * num2
expo = num1 ** num2
sub =  num1 - num2
resto = num1 %2 
# aqui temos as operacoes incluindo exponencial e o resto da divisão 

print("resultado da soma", num1, "+", num2, "é:", soma)
print("resultado da divi", num1, "/", num2, "é:", divi)
print("resultado da divisão inteira", num1, "//", num2, "é", divisao_inteira)
print("resultado da mult", num1, "*", num2, "é:", mult)
print("resultado da exponenciação", num1, "**", num2, "é", expo)
print("resultado da sub", num1, "-", num2, "é:", sub)
print("resultado do resto", num1, "/", num2, "é", resto)
# print dos resultados das operacoes 
print()
print(30*"-","operadores de comparacao",30*"-")
# operadores de compaaração
num1 > num2
num1 > num2
num1 == num2 
num1 >= num2 
num1 <= num2 
num1 != num2 

ano = 2025 
print("ano atual", ano )
ano += 1
print("ano acrecido de +1", ano )
ano -= 1
print("ano decrecido de -1", ano )
 
# operadores logicos 
# AND, OR, NOT
 
 # entrada de dados 

print()
print(30*"-","entrada de dados",30*"-")

nome_usuario = input("digite o seu nome: ")
print("seja bem-vindo ao sistema python", nome_usuario)

print()
print(30*"-","calculadora",30*"-")
numero1 = int(input("digite o primeiro numero: "))
numero2 = int(input("digite o segundo numero: "))

soma = numero1 + numero2
divi =  numero1 / numero2
mult =  numero1 * numero2
sub =  numero1 - numero2
 

print("resultado da soma", numero1, "+", numero2, "é:", soma)
print("resultado da divi", numero1, "/", numero2, "é:", divi)
print("resultado da mult", numero1, "*", numero2, "é:", mult)
print("resultado da sub", numero1, "-", numero2, "é:", sub)

# tipos de dados 
#float = numeros reais, ou seja, tem ",', exe,plo: 5.20
#int = numeros inteiros 
# str = texto, conjunto de caracteres
# bool = valores logicos como true e false 
'''
print()
print(30*"-","convertendo tipos de dados",30*"-")

ano_nascimento = input("digite sua ano de nascimento ")
print(type(ano_nascimento))
#convertendo para inteiro
ano_nascimento = int(ano_nascimento)
print(type(ano_nascimento))

n1 = 19
n2 = 20 

print("a soma é:", n1+n2, type (n1), float(n2))
saudacao = input("digite seu nome:")
cpf =  input("digite seu cpf:")
telefone =  input("digite seu telefone: ")

print(20*"-","dados pessoais",20*"-")
print("nome:", saudacao)
print("cpf:", cpf, "|telefone:",telefone)
print(50*"")