# O - Principio Aberto/Fechado (OCP)
## "Um artefato de software deve estar aberto para extensão, mas fechado para modificações"
### Em outras palavras, o comportamento de um artefato de software deve ser extensível sem ter que modificar esse artefato


class Programer:
    def make(self):
        print("Programmer creating code")


class Seller:
    def make(self):
        print("Seller selling the product")


class RH:
    def make(self):
        print("HR hiring new devs")


class Company:
    def do_work(self, worker: any) -> None:
        worker.make()


programmer = Programer()
seller = Seller()
rh = RH()
company = Company()
company.do_work(programmer)
company.do_work(seller)
company.do_work(rh)
