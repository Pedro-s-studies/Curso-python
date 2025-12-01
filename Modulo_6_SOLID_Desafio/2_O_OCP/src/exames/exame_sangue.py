from .exame_aprovavel import ExameAprovavel


class ExameSangue(ExameAprovavel):
    def aprovar(self):
        # Aqui iriam as validações específicas do exame
        print("Exame sanguíneo aprovado!")
