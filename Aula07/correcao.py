conta = {}
proximo_numero = 1001

def exibir_dados():
    if not conta:
        print('nenhuma conta encontrada!')
        return
    for numero, dados in conta.items(): 
        print()
        print(f'{20*'-'}dados bancarios {20*'-'}')
        print(f'contas: {numero}')
        print(f'saldo:{dados['saldo']}')
        print(f'clientes{dados['nome']} | CPF: {dados['cpf']}')
        print(f'{57*'-'}')
        print()

def criar_conta():
    global proximo_numero
    nome = input('digite seu nome ').strip()
    cpf = input ('digite seu cpf:').strip()
    conta[proximo_numero] = {'nome': nome, ' saldo':0.0, 'cpf':cpf }
    print(f'conta criada com sucesso! numero da conta: {proximo_numero}')
    proximo_numero += 1 

def deposito():
    numero = int(input('digite o numero da conta'))
    if numero in conta:
        valor = float (input('digite o valor que deseja depositar:')).replace(',','.')
        conta[numero]['saldo'] += valor 
        print(f'deposito de R${valor:.2f}realizado com sucesso na conta {numero}')
    else:
        print('conta nao encontrada')
def sacar():
    