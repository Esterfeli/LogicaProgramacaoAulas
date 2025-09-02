def criar_conta (nome, cpf , telefone , email , senha, saldo_inicial = 0):
      print(f'{'-'*20} Olá {nome}, seja bem vindo ao seu novo banco  {'-'*20}')
      print('seu saldo inicial e de R${saldo_inicial : 0,00}')
      return saldo_inicial 
     
nome = input ('digite seu nome :')
cpf = input ('digite seu CPF :')
telefone = input ('digite seu telefone :')
email = input ('digite seu email:')
senha = input ('digite a sua semha :')

def depositar ( valor_deposito , saldo): 
    if valor_deposito > 0:
        saldo += valor_deposito 
        print('voce depositou R$(valor_deposito: 0,00)')
    else: 
        print('valor atualizado com sucesso ')
        return saldo
def sacar  (valor_saque, saldo):
    if valor_saque > 0 and valor_saque <= saldo:
        saldo -= valor_saque
        print(f'voce sacou R${valor_saque: 0,00}')
    else: 
        print('valor indisponivel para saque')
        return saldo 
def encerrar_conta (nome):
                print(f'conta de {nome} encerrar com sucesso :')
                print('obrigado por usar nossos servicos')






