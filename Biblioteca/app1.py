import os
import json

class Livro:
    def __init__(self, id, titulo, autor ,ano):
        self.id= id
        self.titulo  = titulo 
        self.autor = autor
        self.ano = ano 

    @property
    def id(self):
          return self.__id
     
    @property
    def titulo (self):
            return  self.__titulo
    
    @titulo.setter  
    def titulo (self, titulo):
        self.__titulo  = titulo
          
    @property
    def autor (self):
            return  self.__autor
    
    @autor.setter  
    def autor(self, autor):
        self.__autor = autor

    @property
    def ano (self):
            return  self.__ano
    
    @ano.setter  
    def ano(self, ano):
        self.__ano = ano

    def to_dict(self):
        return{
            "id": self.id,
             "titulo":self.titulo,
                "autor":self.autor,
                "ano":self.ano 
            
        }

    def salvar(self):
         with open ("C:\Users\EsterVenturaFelix\Desktop\Lógicaprogramaçãoaula\Aula11/bib.json", "r", encoding="utf-8")as f:
            biblioteca = dict(json.load(f))
            biblioteca["livros"].append({
                "titulo":self.titulo,
                "autor":self.autor,
                "ano":self.ano 
            })

class Biblioteca:
   def __init__(self, arquivo_json ="biblioteca.json"):
      self.__arquivo = arquivo_json
      self.__livro = []
      self.carregar_dadoos()

   def carregar_dados(self):
         if os.path.exists(self.__arquivo):
             with open (self.__arquivo, "r" , encoding="UTF-8") as f:
                 dados = json.load(f)

                 for d in dados:
                     livro = Livro(d['id'], d['titulo'], d ['autor'], d ['ano'])
                     self.__livro.append(livro)
   def salvar_dados(self):
       dados = []
       for livro in self.__livro:
         dados.append(livro.to_dict())
         with open(self.__arquivo, "w" , encoding='UTF-8') as f:
               json.dump( dados,f,indent=4,ensure_ascil=False)
      
   def gerar_id(self):
       if not self.__livros:
           return 1 
       return max( l.id for l in self.__livros)+1 

   def cadastrar_livro(self, titulo,autor,ano):
      novo_livro = Livro(self.gerar_id(),titulo,autor,ano)
      self.__livro.append(novo_livro)
      self.salvar_dados
      print(f'livro: {titulo} cadastrado com sucesso!')

   def listar_livros(self):
      if not self.__livros:
             print('nenhum livro encontrado!')
      else:
         print('n/lista de livros')
      for livro in self.__livros:
         print(f'ID:{livro.id}|titulo: {livro.titulo}| autor: {livro.autor}| ano: {livro.ano}')

   def atualizar_livros(self, id_livro, novo_titulo=None, novo_autor=None, novo_ano= None):
        for livro in self.__livros:
            if livro.id_livro == id_livro:
                if novo_titulo:
                    livro.titulo = novo_titulo
                if novo_autor:
                    livro.autor = novo_autor
                if novo_ano:
                    livro.ano = novo_ano
                self.salvar_dados()
                print("Livro atualizado com sucesso!")
                return
        print("⚠ Livro não encontrado.")
         
   def excluir_livro (self, id_livro):
            for livro in self.__livros:
                if livro.id_livro == id_livro:
                    self.__livros.remove(livro)
                    self.salvar_dados()
                    print("🗑 Livro removido com sucesso!")
                    return
            print("⚠ Livro não encontrado.")
       
       
       


            