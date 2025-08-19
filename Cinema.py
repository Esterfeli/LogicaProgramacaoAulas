sala1 = 'turma da monica'
min1 = 0 
sala2 = 'vingadores'
min2 = 14
sala3 = 'batman'
min3 = 16
sala4 = 'super man'
min4 = 18
sala5 = 'gente grande'
min5 = 16

while True: 
    print(30*'-','cineclub',30*'-')
    print('escolhe uma opcao de filme que deseja assistir!')
    print(f'1. sala 01 - {sala1} idade minima {min1}')
    print(f'2. sala 02 - {sala2} idade minima {min2}')
    print(f'3. sala 03 - {sala3} idade minima {min3}')
    print(f'4. sala 04 - {sala4} idade minima {min4}')
    print(f'5. sala 05 - {sala5} idade minima {min5}')
    print(f'6. sair')

    opção = int(input('digite a opção desejada:'))
    idade = input('digite dua idade:')
    if opção == 1:
        if idade <= min1:
         print('bem vindo ao cineclub')
        print(f'ingresso para: {sala1}')
        print(f'sala: 01')
        break
        

    elif opção == 2:
        print('bem vindo ao cineclub')
        print(f'ingresso para: {sala2}')
        print(f'sala: 02')
        break
        

    elif opção == 3:
        print('bem vindo ao cineclub')
        print(f'ingresso para: {sala3}')
        print(f'sala: 03')
        break

    elif opção == 4:
        print('bem vindo ao cineclub')
        print(f'ingresso para: {sala4}')
        print(f'sala: 04')
        break
    

    elif opção == 5:
        print('bem vindo ao cineclub')
        print(f'ingresso para: {sala5}')
        print(f'sala: 05')
        break

    elif opção == 6:
        print('saindo do sistema')
    else: 
        print('opção invalida!')
