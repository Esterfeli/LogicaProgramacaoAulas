class personagem:
    def __init__(self, nome, vida ):
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

    def atacar(self, personaguem):
         personaguem.vida -= 300
         print(f'{self.nome} atacou {personaguem.nome} e tirou 300 pontos de vida.')
         print(f'agora esta com {personaguem.vida}')
    def dano(self, personagem):
         personagem.vida -= 500
         print(f'{self.nome} atacou {personagem.nome} e tirou 500 pontos de vida.')
         print(f'agora esta com {personagem.vida}')
        
personagem1 = personagem('corinca' , 2000)
print(f'personagem {personagem1.nome}')
print(f'vida: {personagem1.vida}')

personagem2 = personagem('batman' , 3000)
print(f'personagem:{personagem1.nome}')
print(f'vida: {personagem2.vida}')

personagem1.dano(personagem2)
personagem2.atacar(personagem1)
personagem1.dano(personagem2)
personagem2.atacar(personagem1)
personagem1.dano(personagem2)
personagem2.atacar(personagem1)
personagem1.dano(personagem2)
personagem2.atacar(personagem1)
personagem1.dano(personagem2)
personagem2.atacar(personagem1)
personagem1.dano(personagem2)
personagem2.atacar(personagem1)
 
if personagem2.vida >= 1:
      print(f'derrotado com sucesso!{personagem1.nome}')
elif personagem1.vida >= 1:
      print(f'deerotado com sucesso!{personagem2.nome}')
else:
      pass




        
    
