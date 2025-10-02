#classe- espaco onde vou descrever do objeto 
# metodo - que sao as acoes desse objeto 
# atributo - caracteristica do objeto 
# nome e vida - atacar 
# self - quando quero me referir a algum atributo da class
#construtor - quando quero criar um novo objeto , chamo um construtor para acessar os atritutos

class personagem:
     #construtor 
    def __init__(self, nome, vida):
         #encapsulamento
         self.__nome = nome
         self.__vida = vida 

          #definino get e set 
    @property
    def nome (self):
          return self.__nome
     
     # definindo set 
    @nome.setter
    def nome (self , novo_nome):
          self.__nome = novo_nome 
          
    @property
    def vida (self):
            return  self.__vida 
    
    @vida.setter  
    def vida (self, vida):
        self.__vida = vida 
        
    def atacar(self, personaguem):
         personaguem.vida -= 20 
         print(f'{self.nome} atacou {personaguem.nome}e tirou 20 pontos de vida.')
         print(f'agora esta com {personaguem.vida}')

personagem1 = personagem('Gandof' , 100)
print(f'personagem {personagem1.nome}')
print(f'vida: {personagem.vida}')

personagem2 = personagem('legolas' , 100)
print(f'personagem:{personagem1.nome}')
print(f'vida: {personagem2.vida}')

personagem1.atacar(personagem2)
personagem2.atacar(personagem1)

class guerreiro(personagem):
     def __init__(self, nome, vida, escudo=False):
          super().__init__(nome, vida)
          self.__escudo = escudo

     @property
     def escudo(self):
          return self.__escudo
          
     @escudo.setter 
     def escudo(self, escudo):
          self.__escudo = escudo 
          
     def atacar(self,personagem):
          personagem.vida -= 40
          print(f'{self.nome}atacou {personagem.nome} e tirou 40 pontos de vida.')
          print(f'agora esta com {personagem.vida}')

     def proteção(self, personagem):
          self.__vida += 10  
    
class mago(personagem):
     def __init__(self, nome, vida):
          super().__init__(nome, vida)
          def curar(self, personagem ):
               personagem.vida += 15 
               print(f'{self.__nome} usou poder de curar em {personagem.nome }')
               print(f'a vida de {personagem.nome}agora e de{personagem.vida} ')
              
          def atacar(self,personagem):
               personagem.vida -= 30 
               print(f'{self.nome}atacou {personagem.nome} e tirou 40 pontos de vida.')
               print(f'agora esta com {personagem.vida}')


frodo= personagem('frodo' , 100)
gandof = mago('Gadof' , 100)
aragorn = guerreiro('aragorn' , 100)

aragorn.atacar(frodo)
gandof.curar(frodo)
gandof.atacar(aragorn)
aragorn.atacar(gandof)
gandof.curar(gandof)
frodo.atacar (aragorn)