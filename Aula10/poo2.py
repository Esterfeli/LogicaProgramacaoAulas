class personagem:
    def __init__(self, nome, vida):
         self.__nome = nome
         self.__vida = vida 

          
    @property
    def nome (self):
          return self.__nome
     
    @nome.setter
    def nome (self , novo_nome):
          self.__nome = novo_nome 
          
    @property
    def vida (self):
            return  self.__vida 
    
    @vida.setter  
    def vida (self, vida):
        self.__vida = vida 
        
    def atacar(self, personagem):
         personagem.vida -= 200
         print(f'{self.nome} atacou {personagem.nome}e tirou 200 pontos de vida.')
         print(f'agora esta com {personagem.vida}')

    def torre(self, personagem):
         personagem.vida -= 400
         print(f'{self.nome} atacou {personagem.nome}e tirou 500 pontos de vida.')
         print(f'agora esta com {personagem.vida}')

personagem1 = personagem('arqueiro', 800)
print(f'personagem {personagem1.nome}')
print(f'vida: {personagem.vida}')

personagem2 = personagem('cavaleiro' , 500)
print(f'personagem:{personagem1.nome}')
print(f'vida: {personagem2.vida}')

personagemFavorito = personagem('flash', 1000)
print(f'personagem:{personagemFavorito.nome}')
print(f'vida: {personagemFavorito.vida}')


personagem1.atacar(personagem2)
personagem2.atacar(personagem1)
personagem1.atacar(personagemFavorito)
personagem2.atacar(personagemFavorito)
personagemFavorito.torre(personagem1)
personagemFavorito.torre(personagem2)

