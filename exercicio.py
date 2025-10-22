class Animal:
    def __init__(self, nome: str, idade:int):
        self.nome=nome
        self.idade=idade

    def emitir_som(self):
        print("O Animal emite som.")

    def apresentar(self):
        print(f"Olá, sou {self.nome} e tenho {self.idade}")

class Cachorro(Animal):
    def __init__(self, nome:str, idade:int, raca:str):
        super().__init__(nome, idade)
        self.raca=raca

    def emitir_som(self):
        return "Au! Au!"

class Gato(Animal):
    def __init__(self, nome:str, idade:int, cor_pelo:str):
        super().__init__(nome,idade)
        self.cor_pelo=cor_pelo

    def emitir_som(self):
        return "Miau!"

class Vaca(Animal):
    def __init__(self, nome:str, idade:int, producao_leite_litros:float):
        super().__init__(nome,idade)
        self.__producao_leite_litros=producao_leite_litros

    def emitir_som(self):
        return "Muuu!" 

    def obter_producao_leite(self):
        return self.__producao_leite_litros
    
    def registrar_ordenha(self, litros:float):
        self.__producao_leite_litros=litros
        print(f"A nova produção de leite foi de {self.__producao_leite_litros}")

cachorro = Cachorro("Rex", 3, "Labrador")
gato = Gato("Mimi", 5, "Branco")
vaca = Vaca("Mimosa", 7, 25.5)

animais=[cachorro,gato,vaca]

for animal in animais:
    print(animal.apresentar())
    print(animal.emitir_som())

    if isinstance (animal, Cachorro):
        print(f"Minha raça é: {animal.raca}")
    if isinstance(animal.Gato):
        print(f"O meu pelo é: {animal.cor_pelo}")
    if isinstance(animal.Vaca):
        print(f"A minha produção de leite é:  {animal.obter_producao_leite()}")
    