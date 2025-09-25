from classe import Biblioteca

def main ():
    biblioteca = Biblioteca()
    while True:

        print(20*"-" ,"MENU", 20*"-")
        print('1 - Cadastrar ') 
        print('1 - listar  ') 
        opcao = input("digite uma opcao:")

        if opcao == "1":
            titulo = input("TItulo")
            autor = input("autor")
            try:
                ano = int(input("ANO:"))
                biblioteca.cadastrar_livro(titulo,autor,ano)
            except ValueError:
                print("Ano invalido")
        elif opcao == "2":
            biblioteca.listar_livros()

if __name__ == "__main__":
    main()