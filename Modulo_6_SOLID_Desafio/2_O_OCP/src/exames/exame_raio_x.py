from .exame_aprovavel import ExameAprovavel


class ExameRaioX(ExameAprovavel):
    def aprovar(self):
        # Aqui iriam as validações específicas do exame
        print("Exame de Raio-X aprovado!")
