# L - Principio de Substituição de Liskov (LSP)
## "Objetos podem ser substituídos por seus subtipos sem que isso afete a execução correta do programa"
### O LSP pode e deve ser estendido ao nível da arquitetura. Uma simples violação de substituição pode fazer com que a arquitetura de um sistema seja poluída com uma quantidade significativa de mecanismos extras.


class Animal:
    def comer(self):
        print("O Animal comendo")

    def andar(self):
        print("O animal está andando na jaula")


class Felino(Animal):
    def lamber(self):
        print("O Felino está lambendo seu pelo")


class Leao(Felino):
    def rugir(self):
        print("O leao esta rugindo alto !!!")


class Pessoa:
    def observa(self, animal: Animal):
        animal.comer()


renatinho = Pessoa()
animal = Animal()
felino = Felino()
leao = Leao()

renatinho.observa(leao)
